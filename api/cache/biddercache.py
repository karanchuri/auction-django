from api.adapter.redis.rediscacheadapter import RedisCacheAdapter
from api.adapter.redis.basecachehandler import BaseCacheHandler


class BidderCache(BaseCacheHandler):

    def __init__(self):
        self.key = "bidding_list"
        super().__init__(key=self.key, timeout=60 * 60 * 12)

    def get_configuration(self):
        _cached_content = RedisCacheAdapter.get(
            self.key, machine_alias=self.machine_alias
        )
        print(_cached_content)
        if not _cached_content:
            return []
        return _cached_content

    def delete_collection(self):
        RedisCacheAdapter.delete_collection(
            start_search="catalogue_cache",
            machine_alias=self.machine_alias
        )
