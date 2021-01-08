from elasticsearch import AsyncElasticsearch

from app.core.config import get_settings


class Database:
    client: AsyncElasticsearch = None


_db = Database()


def get_client() -> AsyncElasticsearch:
    return _db.client


async def connect():
    settings = get_settings()
    hosts = settings.es_hosts
    opts = {}
    if (settings.es_user is not None and settings.es_password is not None):
        opts["http_auth"] = (settings.es_user, settings.es_password)
    _db.client = AsyncElasticsearch(hosts, **opts)


async def close():
    await _db.client.close()