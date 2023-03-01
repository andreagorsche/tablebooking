from django.shortcuts import render
from django.views import generic
from .models import Reservation

class ReservationList (generic.ListView):
    model = Reservation
    queryset = Reservation.object.filter(Guest)