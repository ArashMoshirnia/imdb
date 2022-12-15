from celery import shared_task


@shared_task
def send_sms_to_user(phone_number):
    print(f'sms sent: {phone_number}')
    return True
