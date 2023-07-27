from django.shortcuts import render
from .models import Table, Reservation
from django.http import HttpResponse
from datetime import datetime
from django.views.generic.edit import CreateView, DeleteView
from django.views import generic
from django.urls import reverse_lazy
from .forms import ReservationForm


def base(request):
    return render(request, 'tablebooking/base.html')

def login(request):
    return render(request, 'tablebooking/menu.html')

class CreateReservation(CreateView):
    model = Reservation
    template_name = "tablebooking/create_booking.html"
    success_url = reverse_lazy('home')
    form_class = ReservationForm
    
    def form_valid(self, form):
        data = form.cleaned_data
        form.instance.user = self.request.user
        tables = Table.objects.filter(number_of_seats__gte=form.instance.number_of_guests)
        if tables.exists():
                form.instance.table = tables.first()
        return super().form_valid(form)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Reservation

class ReservationList(LoginRequiredMixin, generic.ListView):
    model = Reservation
    template_name = "tablebooking/list_booking.html"
    paginate_by = 5

# Filter reservations based on the currently logged-in user
    def get_queryset(self):
        user = self.request.user
        queryset = Reservation.objects.filter(user=user)
        return queryset


class ReservationUpdate (generic.UpdateView):
    model = Reservation
    fields = ('date', 'time', 'number_of_guests', 'number_of_child_seats', 'comment')
    template_name = "tablebooking/manage_booking.html"
    success_url = reverse_lazy('list_reservation') 

class ReservationDelete(DeleteView):
    model = Reservation
    success_url = reverse_lazy('list_reservation') 