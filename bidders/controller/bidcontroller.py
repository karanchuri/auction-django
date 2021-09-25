import requests
import threading
import random
import time


class BidController(threading.Thread):

    def __init__(self, bid_id, bidder_id):
        threading.Thread.__init__(self)
        self.bid_id = bid_id
        self.bidder_id = bidder_id

    def run(self):
        sleep_milli = random.randint(10, 50) / 1000
        time.sleep(sleep_milli)
        value = random.randint(10, 1000000)
        response = requests.post(url="http://auction-system-main:9000/api/auctionms/api/create-bid", data={
            "value": value,
            "bid_id": self.bid_id,
            "bidder_id": self.bidder_id
        })
        print(response.status_code)
