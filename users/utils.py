import random
import string

from django.core.cache import cache
from django.conf import settings

from utils.sms_messages import send_message


def generate_otp_code():
    return ''.join(random.choices(string.digits, k=5))


def send_otp_to_user(user):
    otp = generate_otp_code()
    res = send_message(user.phone_number, f'Your otp code is {otp}')
    if not res:
        return False

    cache_key = f'otp_code:{user.phone_number}'
    cache.set(cache_key, otp, settings.OTP_CODE_VALIDATION_TIME)

    return True
