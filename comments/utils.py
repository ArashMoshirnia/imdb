from django.conf import settings

from comments.models import CurrencyExchangeRate
from utils.redis.connection import get_redis_client


def update_exchange_rates_in_redis():
    exchange_rates = CurrencyExchangeRate.objects.all()
    redis_client = get_redis_client()
    mapping = {f'{ex_rate.currency_from}/{ex_rate.currency_to}': ex_rate.rate for ex_rate in exchange_rates}
    redis_client.hset(settings.REDIS_EXCHANGE_RATE_HASHMAP_NAME, mapping=mapping)
