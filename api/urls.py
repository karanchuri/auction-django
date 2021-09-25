from django.urls import path
from api import views

urlpatterns = [
    path("health", views.HealthView.as_view(), name="health"),
    path("create-auction", views.CreateAuctionView.as_view(), name="auction"),
    path("create-bid", views.CreateBid.as_view(), name="bid"),
    path("clear-bid-channel", views.ClearBidChannelView.as_view(), name="clear_bid"),
]
