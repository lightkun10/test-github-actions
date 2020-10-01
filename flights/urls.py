from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # For specific flight
    path("<int:flight_id>", views.flight, name="flight"),
    # Book a flight for a particular flight ID
    path("<int:flight_id>/book", views.book, name="book")
]