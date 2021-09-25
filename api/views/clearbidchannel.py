from api.cache.biddercache import BidderCache
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class ClearBidChannelView(APIView):

    def get(self, request):
        BidderCache().invalidate_cache()
        return Response(status=status.HTTP_200_OK)

