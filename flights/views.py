from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Flight, Passenger

# Create your views here.
def index(request):
    # Display the list of all flights
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    # Get the flight from the id of 
    # the flight that being selected by user
    flight = Flight.objects.get(pk=flight_id) # pk=primary key

    # Pass the flight data to the HTML template
    return render(request, "flights/flight.html", {
        # What flight is being rendered
        "flight": flight,
        # Who are the passengers
        "passengers": flight.passengers.all(),
        # Who are the passengers that is not included in
        # current rendered flight
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })

def book(request, flight_id):
    # If user submitted the form 
    # via the post request method...
    if request.method == "POST":
        # Get the particular flight from the
        # given flight ID
        flight = Flight.objects.get(pk=flight_id)
        # Get the passenger, where's ID is equal to
        # whatever submitted via post form for a field
        # with the name of "passenger"
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        # Add the particular flight to the passenger list of flights
        passenger.flights.add(flight)
        
        # Redirect user to flight page after submitting the form
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
        # reverse takes the name of a particular view defined in
        # urls.py, and gets me what the actual URL path should be.