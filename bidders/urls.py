from django.conf.urls import url
from bidders import views

urlpatterns = [
    url(r"health/+$", views.HealthView.as_view(), name="health"),
]
