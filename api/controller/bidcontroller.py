from api.cache.auctioncache import AuctionCache


class BidController:

    def __init__(self, data):
        self.data = data
        self._parse_data()

    def _parse_data(self):
        self.auction_id = self.data.get("bid_id")
        self.bidder_id = self.data.get("bidder_id")
        self.value = int(self.data.get("value"))

    def bid_to_auction(self):
        cache = AuctionCache(auction_id=self.auction_id)
        config = cache.get_configuration()
        if not config:
            return None
        if self.value > config["value"]:
            config["bidder_id"] = self.bidder_id
            config["value"] = self.value
            cache.set_configuration(content=config)
            return True
        return False
