from django.conf import settings

from utils.redis.connection import get_redis_client


def retrieve_exchange_rate_from_redis(currency_from, currency_to):
    redis_client = get_redis_client()
    rate = redis_client.hget(settings.REDIS_EXCHANGE_RATE_HASHMAP_NAME,
                             f'{currency_from}/{currency_to}')
    return float(rate)
