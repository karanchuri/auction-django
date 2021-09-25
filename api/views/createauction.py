from api.controller.auctioncreatecontroller import AuctionCreateController
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import time


class CreateAuctionView(APIView):

    def get(self, request):
        auction_id = int(request.query_params.get("auction_id", -1))
        if auction_id == -1:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        controller = AuctionCreateController(auction_id=auction_id)
        controller.create_auction()
        controller.create_bid_channel()
        time.sleep(2/10)
        data = controller.get_winner_of_bid()
        controller.reset_all()
        return Response(status=status.HTTP_200_OK, data=data)
