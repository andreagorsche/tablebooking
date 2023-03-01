from django.shortcuts import render
from django.views import generic
from .models import Reservation, Guest

class ReservationList (generic.ListView):
    model = Reservation
    queryset = Reservation.object.filter(username)order_by('-date')
    template_name = "manage_reservations.html"
    paginate_by = 5