from django.core.management import BaseCommand
from comments.models import CurrencyExchangeRate
from comments.utils import update_exchange_rates_in_redis

# * * * * *  /home/arash/PycharmProjects/imdb/venv/bin/python /home/arash/PycharmProjects/imdb/manage.py update_exchange_rates

def get_latest_exchange_rates():
    return [
        {'currency_from': 'USD', 'currency_to': 'IRR', 'rate': 460_000}
    ]


class Command(BaseCommand):
    def handle(self, *args, **options):
        latest_exchange_rates = get_latest_exchange_rates()

        updated_instances = []
        for new_exchange_rate in latest_exchange_rates:
            # CurrencyExchangeRate.objects.update_or_create(
            #     currency_from=new_exchange_rate['currency_from'],
            #     currency_to=new_exchange_rate['currency_to'],
            #     defaults={'rate': new_exchange_rate['rate']}
            # )

            try:
                exchange_rate = CurrencyExchangeRate.objects.get(
                    currency_from=new_exchange_rate['currency_from'],
                    currency_to=new_exchange_rate['currency_to']
                )
                exchange_rate.rate = new_exchange_rate['rate']
                updated_instances.append(exchange_rate)

            except CurrencyExchangeRate.DoesNotExist:
                CurrencyExchangeRate.objects.create(
                    currency_from=new_exchange_rate['currency_from'],
                    currency_to=new_exchange_rate['currency_to'],
                    rate=new_exchange_rate['rate']
                )

        if updated_instances:
            CurrencyExchangeRate.objects.bulk_update(updated_instances, fields=['rate'])

        update_exchange_rates_in_redis()
