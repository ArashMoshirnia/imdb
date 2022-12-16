from celery.exceptions import MaxRetriesExceededError
from django.utils import timezone
from celery import shared_task


def send_kavehnegar_sms(phone_number, success=True):
    if not success:
        raise ConnectionError
    return success


@shared_task(bind=True, autoretry_for=(ConnectionError,), max_retries=3, default_retry_delay=5)
def send_sms_to_user(self, phone_number):
    try:
        result = send_kavehnegar_sms(phone_number, success=False)
    except ConnectionError:
        print('task failed')

    # if not result:
    #     try:
    #         raise self.retry()
    #     except MaxRetriesExceededError:
    #         print('task failed')

    return result


def run_task():
    send_sms_to_user.delay(989120520994)

    a_minute_later = timezone.now() + timezone.timedelta(minutes=1)
    send_sms_to_user.apply_async([989120520994], eta=a_minute_later)
