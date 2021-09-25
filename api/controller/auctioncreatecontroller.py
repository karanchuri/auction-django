from api.cache.auctioncache import AuctionCache
from api.cache.biddercache import BidderCache


class AuctionCreateController:

    def __init__(self, auction_id):
        self.auction_id = auction_id
        self.cache = None

    def create_auction(self):
        self.cache = AuctionCache(auction_id=self.auction_id)
        if self.cache.get_configuration():
            return None
        self.cache.set_configuration({
            "bidder_id": -1,
            "value": -1
        })
        return True

    def create_bid_channel(self):
        old_config = BidderCache().get_configuration()
        if self.auction_id in old_config:
            return False
        old_config.append(self.auction_id)
        BidderCache().set_configuration(content=old_config)
        return True

    def reset_all(self):
        self.cache.invalidate_cache()
        old_config = BidderCache().get_configuration()
        try:
            old_config.remove(self.auction_id)
            BidderCache().set_configuration(content=old_config)
        except:
            pass

    def get_winner_of_bid(self):
        return self.cache.get_configuration()
