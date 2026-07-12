from redis.asyncio import Redis
from aiohttp.web import Application


def setup_redis(app: Application):
    conf = app['config']['redis']
    app['redis'] = Redis(host=conf['host'], port=conf['port'], db=conf['db'])
    app.on_cleanup.append(_close_redis)


async def _close_redis(app: Application):
    await app['redis'].aclose()
