from django.conf.urls import include, url


urlpatterns = [
    url("api/auctionms/api/", include("api.urls")),
]
