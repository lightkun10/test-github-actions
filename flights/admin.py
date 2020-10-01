from django.contrib import admin
from .models import Flight, Airport, Passenger

# Register your models here.

# Custom ui info
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

class AirportAdmin(admin.ModelAdmin):
    list_display = ("id", "city", "code")

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

admin.site.register(Airport, AirportAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)