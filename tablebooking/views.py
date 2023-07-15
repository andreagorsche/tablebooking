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
        tables = Table.objects.filter(number_of_seats__gte=form.instance.number_of_guests)
        return super().form_valid(form)

''' validate the entered date

    def validate_date(date):
        # Check if data was entered
        if not date:
            raise ValidationError("This field cannot be left blank")

        # Check if the date string matches the format "dd/mm/yyyy"
        try:
            validate_date = datetime.strptime(date, "%d/%m/%Y").date()
        except ValueError:
            raise ValidationError("Incorrect date format. Please use the format dd/mm/yyyy")

        # Check if date is not in the past
        today = datetime.today().date()
        if validate_date < today:
            raise ValidationError("Booking date can't be in the past")

        return validated_date'''
    

def login(request):
    return render(request, 'tablebooking/menu.html')


def manage_booking(request):
    return render(request, 'tablebooking/manage_booking.html')
