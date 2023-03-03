from django.shortcuts import render
from .models import Reservation
from django.http import HttpResponse
from datetime import datetime


def base(request):
    return render(request, 'tablebooking/base.html')


def booking_form(request):
    if request.method == 'Post':
        date = request.Post['date']
        time = request.Post['time']
        no_of_people = request.Post['no_of_people']
        no_of_child_seats = request.Post['no_of_child_seats']
        private_booth = request.Post['private_booth']

        new_reservation = Reservation(date=date, time=time, people=no_of_people, kids=no_of_child_seats, private=private_booth)
        new_reservation.save()

    return render(request, 'tablebooking/booking_form.html')


def login(request):
    return render(request, 'tablebooking/menu.html')


def manage_booking(request):
    return render(request, 'tablebooking/manage_booking.html')
