from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.conf import settings


class HealthView(APIView):

    def get(self, request):
        return Response(status=status.HTTP_200_OK,
                        data={"status": f"I am healthy auctionms {settings.FLAVOUR} Microservice :)"})

