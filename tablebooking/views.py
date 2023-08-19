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
    """
    Base function rendering the base html template.
    """
    return render(request, 'tablebooking/base.html')


@login_required
def confirm_reservation(request):
    """
    Function to render the reservation confirmation page.
    User login is required, restricted access.
    """
    return render(request, 'tablebooking/reservation_confirm.html')


@login_required
def confirm_reservation_update(request):
    """
    Function to render the confirmation page after updating a reservation.
    User login is required, restricted access.
    """
    return render(request, 'tablebooking/reservation_confirm_update.html')


@login_required
def delete_confirmed(request):
    """
    Function to render the reservation deleted confirmation page.
    User login is required, restricted access.
    """
    return render(request, 'tablebooking/delete_confirmed.html')


@login_required
def waitlist_confirmed(request):
    """
    Function to render the waitlist confirmation page.
    User login is required, restricted access.
    """
    return render(request, 'tablebooking/waitlist_confirmed.html')


@method_decorator(login_required, name='dispatch')
class CreateReservation(CreateView):
    """
    Class-based view to create reservations based on the Reservation model,
    ReservationForm, rendering the create_booking.html
    and directing to the success url reservation confirmed.
    User login is required, restricted access.
    """
    model = Reservation
    template_name = "tablebooking/create_booking.html"
    success_url = reverse_lazy('confirm_reservation')
    form_class = ReservationForm

    def form_valid(self, form):
        """
        Checking if overlapping reservations exist and handling the
        possible scenarios in the if else statements from line 85 to 104.
        If an overlapping reservation exists and the user ticked the
        Waitlist checkbox, assign a table, save the reservation and
        return the waitlist confirmed template.
        Else throw an error and return an invalid form.
        If there are no overlapping reservations (elif), assign the first
        free table, save the reservation, and return the booking confirmation
        template.
        """
        data = form.cleaned_data
        form.instance.user = self.request.user
        tables = Table.objects.filter(
            number_of_seats__gte=form.instance.number_of_guests
            )
        # Check for overlapping reservations
        overlapping_reservations = Reservation.objects.filter(
            table__in=tables, date=data.get("date"), time=data.get("time")
            )
        # Set the is_waitlisted value
        is_waitlisted = self.request.POST.get("is_waitlisted") == 'on'
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
                    " for the selected date and time."
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
    """
    Class-based view to list reservations based on the Reservation model,
    rendering the list_booking.html, paginated by 1.
    User login is required, restricted access.
    """
    model = Reservation
    template_name = "tablebooking/list_booking.html"
    paginate_by = 1
    """
    Filter reservations based on the currently logged-in user.
    Don't show reservations in the past.
    """
    def get_queryset(self):
        user = self.request.user
        d_today = datetime.today().date()
        queryset = Reservation.objects.filter(user=user, date__gte=d_today)
        return queryset


@method_decorator(login_required, name='dispatch')
class ReservationUpdate(generic.UpdateView):
    """
    Class-based view to update reservations based on the ReservationForm,
    rendering the manage_booking.html, directing to the success url
    reservation_confirm_update.html.
    User login is required, restricted access.
    """
    form_class = ReservationForm
    model = Reservation
    template_name = "tablebooking/manage_booking.html"
    success_url = reverse_lazy('conf_upd_reservation')

    def get_form(self, form_class=None):
        """
        Function to get the, parse the date in the format DD/MM/YYYY,
        and set the initial data for the user to update.
        """
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
        """
        Form validation according to the create reservation view, to ensure
        that wrongly entered data of users are checked and feedbacked like
        in the general reservation form. And that overlapping reservations,
        are avoided and users have the option to be waitlisted.
        """
        data = form.cleaned_data
        form.instance.user = self.request.user
        tables = Table.objects.filter(
            number_of_seats__gte=form.instance.number_of_guests
            )
        # Check for overlapping reservations
        overlapping_reservations = Reservation.objects.filter(
            table__in=tables, date=data.get("date"), time=data.get("time")
            )
        # Set the is_waitlisted value
        is_waitlisted = self.request.POST.get("is_waitlisted") == "on"
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
                    " for the selected date and time."
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
class ReservationDelete(DeleteView):
    """
    Class-based view to delete reservations based on the Reservation model,
    directing to the success url reservation_confirm_delete.html.
    User login is required, restricted access.
    """
    model = Reservation
    success_url = reverse_lazy('delete_confirmed')
