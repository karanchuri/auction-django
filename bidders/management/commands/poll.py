from bidders.controller.bidcontroller import BidController
from django.core.management.base import BaseCommand
from api.cache.biddercache import BidderCache
import time


class Command(BaseCommand):
    """
        To run: python3 manage.py poll <bidder_id>
        Where bidder_id is an integer ID
    """
    help = 'Bidder Module'
    SLEEP_INTERVAL = 2 / 1000
    LAST_PROCESSED = -1

    def add_arguments(self, parser):
        parser.add_argument('bidder_id', type=int)

    def handle(self, *args, **options):
        bidder_id = options['bidder_id']
        print(f"Starting Bidder {bidder_id}")
        while True:
            available_bids = BidderCache().get_configuration()
            for bid_id in available_bids[::-1]:
                if bid_id <= self.LAST_PROCESSED:
                    break
                self.LAST_PROCESSED = int(bid_id)
                BidController(bid_id=bid_id, bidder_id=bidder_id).start()
                print(f"Processing {bidder_id} :: {bid_id}")
            time.sleep(self.SLEEP_INTERVAL)
            print(f"Loop {bidder_id}")
