from django.shortcuts import render, redirect
from .models import Table, Reservation
from django.http import HttpResponse
from datetime import datetime, date
from django.views.generic.edit import CreateView, DeleteView
from django.views import generic
from django.urls import reverse_lazy
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def base(request):
    return render(request, 'tablebooking/base.html')


@login_required
def confirm_reservation(request):
    return render(request, 'tablebooking/reservation_confirm.html')


@login_required
def confirm_reservation_update(request):
    return render(request, 'tablebooking/reservation_confirm_update.html')


@login_required
def delete_confirmed(request):
    return render(request, 'tablebooking/delete_confirmed.html')


@login_required
def waitlist_confirmed(request):
    return render(request, 'tablebooking/waitlist_confirmed.html')


@method_decorator(login_required, name='dispatch')
class CreateReservation(CreateView):
    model = Reservation
    template_name = "tablebooking/create_booking.html"
    success_url = reverse_lazy('confirm_reservation')
    form_class = ReservationForm

    def form_valid(self, form):
        data = form.cleaned_data
        form.instance.user = self.request.user
        tables = Table.objects.filter(
            number_of_seats__gte=form.instance.number_of_guests
            )
        # Exclude the current reservation if it's being updated
        overlapping_reservations = Reservation.objects.filter(
            table__in=tables, date=data.get("date"), time=data.get("time")
            )
        is_waitlisted = self.request.POST.get("is_waitlisted") == 'on'
        # Set the is_waitlisted value
        form.instance.is_waitlisted = is_waitlisted
        if overlapping_reservations.exists():
            if is_waitlisted:
                form.instance.table = tables.first()
                form.save()
                return render(
                    self.request, 'tablebooking/waitlist_confirmed.html'
                    )
            else:
                form.add_error(
                    'date',
                    "This table is already booked"
                    "for the selected date and time."
                    "Check the box to be waitlisted."
                    )
                return super().form_invalid(form)
        elif tables.exists():
            form.instance.table = tables.first()
            form.save()  # Save the reservation
            return render(
                self.request, 'tablebooking/reservation_confirm.html'
                )


@method_decorator(login_required, name='dispatch')
class ReservationList(generic.ListView):
    model = Reservation
    template_name = "tablebooking/list_booking.html"
    paginate_by = 1
    """
    Filter reservations based on the currently logged-in user
    and that are not in the past
    """
    def get_queryset(self):
        user = self.request.user
        d_today = datetime.today().date()
        queryset = Reservation.objects.filter(user=user, date__gte=d_today)
        return queryset


@method_decorator(login_required, name='dispatch')
class ReservationUpdate(generic.UpdateView):
    form_class = ReservationForm
    model = Reservation
    template_name = "tablebooking/manage_booking.html"
    success_url = reverse_lazy('conf_upd_reservation')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        # Parse the date from the object and set it in the desired format
        formatted_date = self.object.date.strftime('%d/%m/%Y')

        # Set the initial data for the form fields
        initial_data = {
            'date': formatted_date,
            'time': self.object.time,
            'number_of_guests': self.object.number_of_guests,
            'number_of_child_seats': self.object.number_of_child_seats,
            'comment': self.object.comment,
        }
        form.initial = initial_data
        return form

    def form_valid(self, form):
        data = form.cleaned_data
        form.instance.user = self.request.user
        tables = Table.objects.filter(
            number_of_seats__gte=form.instance.number_of_guests
            )
        # Exclude the current reservation if it's being updated
        overlapping_reservations = Reservation.objects.filter(
            table__in=tables, date=data.get("date"), time=data.get("time")
            )
        if overlapping_reservations.exists():
            form.add_error(
                'date',
                "This table is already booked for the selected date and time."
                )
            return super().form_invalid(form)

        if tables.exists():
            form.instance.table = tables.first()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ReservationDelete(DeleteView):
    model = Reservation
    success_url = reverse_lazy('delete_confirmed')
