from django.shortcuts import render
from .models import Table, Reservation
from django.http import HttpResponse
from datetime import datetime
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import ReservationForm


def base(request):
    return render(request, 'tablebooking/base.html')


class create_booking(CreateView):
    model = Reservation
    template_name = "tablebooking/create_booking.html"
    success_url = reverse_lazy('home')
    form_class = ReservationForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        tables = Table.objects.filter(number_of_people=form.instance.number_of_people)
        return super().form_valid(form)


def login(request):
    return render(request, 'tablebooking/menu.html')


def manage_booking(request):
    return render(request, 'tablebooking/manage_booking.html')
