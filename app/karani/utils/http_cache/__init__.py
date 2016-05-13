from .filesys import FileSysCache
from .data import DataProperty, ResponseData
import requests, requests_cache


def install_cache(cache_dir, expire_after = None, dbname = 'db', backend = 'filesys'):
    requests_cache.install_cache(cache_dir,
            backend = backend, expire_after=expire_after, dbname = dbname)
    response_cache_props()


from requests.models import Response

def response_cache_props():
    Response.data = DataProperty()
