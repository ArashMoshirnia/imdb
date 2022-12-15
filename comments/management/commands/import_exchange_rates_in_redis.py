from django.conf import settings
from django.core.management import BaseCommand
from comments.models import CurrencyExchangeRate
from utils.redis.connection import get_redis_client


class Command(BaseCommand):
    def handle(self, *args, **options):
        exchange_rates = CurrencyExchangeRate.objects.all()
        redis_client = get_redis_client()

        # for ex_rate in exchange_rates:
        #     redis_client.hset('currency_exchange_rates',
        #                       f'{ex_rate.currency_from}/{ex_rate.currency_to}',
        #                       ex_rate.rate)
        #
        mapping = {f'{ex_rate.currency_from}/{ex_rate.currency_to}': ex_rate.rate for ex_rate in exchange_rates}

        redis_client.hset(settings.REDIS_EXCHANGE_RATE_HASHMAP_NAME, mapping=mapping)
