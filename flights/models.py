from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length = 3)
    city = models.CharField(max_length = 64)

    def __str__(self):
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    # origin = models.CharField(max_length = 64)
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, 
                                        related_name="departures")
    # CASCADE means that the row will be deleted 
    # too if the ForeignKey gets deleted.
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, 
                                             related_name="arrivals")
    duration = models.IntegerField()

    # Returns string representation 
    # of a particular object
    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

    # Check if a flight is valid,
    # if its origin and destination is not the same, 
    # and/or its duration is positive
    def is_valid_flight(self):
        # return self.origin != self.destination and self.duration >= 0
        return self.origin != self.destination or self.duration >= 0

class Passenger(models.Model):
    first = models.CharField(max_length = 64)  # first name
    last = models.CharField(max_length = 64)   # last name

    # A flight could have multiple passengers,
    # a passenger could be on multiple flights.
    # I need an additional table to keep track of this
    flights = models.ManyToManyField(Flight, blank=True, 
                                             related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"