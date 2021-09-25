from api.controller.bidcontroller import BidController
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class CreateBid(APIView):

    def post(self, request):
        controller = BidController(data=request.data)
        result = controller.bid_to_auction()
        if result is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        elif result is False:
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_200_OK)
