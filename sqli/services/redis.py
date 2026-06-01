from redis.asyncio import ConnectionPool, Redis
from aiohttp.web import Application


def setup_redis(app: Application):
    app.on_startup.append(_init_redis)
    app.on_shutdown.append(_close_redis)


async def _init_redis(app: Application):
    conf = app['config']['redis']
    pool = ConnectionPool.from_url(
        f"redis://{conf['host']}:{conf['port']}/{conf['db']}"
    )
    app['redis'] = Redis(connection_pool=pool)


async def _close_redis(app: Application):
    await app['redis'].aclose()
