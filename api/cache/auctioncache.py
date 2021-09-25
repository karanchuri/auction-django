from api.adapter.redis.rediscacheadapter import RedisCacheAdapter
from api.adapter.redis.basecachehandler import BaseCacheHandler


class AuctionCache(BaseCacheHandler):

    def __init__(self, auction_id):
        super().__init__(key=f"auction_id_{auction_id}", timeout=60 * 60 * 12)

    def get_configuration(self):
        _cached_content = RedisCacheAdapter.get(
            self.key, machine_alias=self.machine_alias
        )
        if not _cached_content:
            return None
        return _cached_content

    def delete_collection(self):
        RedisCacheAdapter.delete_collection(
            start_search="catalogue_cache",
            machine_alias=self.machine_alias
        )
