import redis.asyncio as aioredis
from aiohttp.web import Application


def setup_redis(app: Application):
    app.on_startup.append(_init_redis)
    app.on_shutdown.append(_close_redis)


async def _init_redis(app: Application):
    conf = app['config']['redis']
    redis = aioredis.Redis(host=conf['host'], port=conf['port'], db=conf['db'])
    app['redis'] = redis


async def _close_redis(app: Application):
    await app['redis'].aclose()
