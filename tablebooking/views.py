from django.shortcuts import render
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
    return render(request, 'tablebooking/waitlisted_confirm.html')

@login_required
def confirmation_waitlist(request):
    return render(request, 'tablebooking/confirmation_waitlist.html')
    
@method_decorator(login_required, name='dispatch')
class CreateReservation(CreateView):
    model = Reservation
    template_name = "tablebooking/create_booking.html"
    success_url = reverse_lazy('confirm_reservation')
    form_class = ReservationForm

    def form_valid(self, form):
        data = form.cleaned_data
        form.instance.user = self.request.user
        tables = Table.objects.filter(number_of_seats__gte=form.instance.number_of_guests)
        overlapping_Reservations = Reservation.objects.filter(table__in=tables, date=data.get("date"), time=data.get("time"))

        if overlapping_Reservations.exists():
            is_waitlisted = self.request.POST.get("is_waitlisted")  # Get the user's choice from the form data
            if is_waitlisted:
                form.instance.is_waitlisted = True  # Mark the reservation as waitlisted
                return super().form_valid(form)
            else:
                return self.form_invalid(form)  # Return form invalid without rendering

        if tables.exists():
            form.instance.table = tables.first()
            return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class ReservationList(generic.ListView):
    model = Reservation
    template_name = "tablebooking/list_booking.html"
    paginate_by = 1

    # Filter reservations based on the currently logged-in user and that are not in the past
    def get_queryset(self):
        user = self.request.user
        d_today = datetime.today().date()
        queryset = Reservation.objects.filter(user=user,date__gte=d_today)
        return queryset

@method_decorator(login_required, name='dispatch')
class ReservationUpdate(generic.UpdateView):
    form_class = ReservationForm
    model = Reservation
    template_name = "tablebooking/manage_booking.html"
    success_url = reverse_lazy('conf_upd_reservation')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        # Set the initial data for the form fields
        initial_data = {
            'date': self.object.date,
            'time': self.object.time,
            'number_of_guests': self.object.number_of_guests,
            'number_of_child_seats' : self.object.number_of_child_seats,
            'comment' : self.object.comment,
        }

        form.initial = initial_data
        return form

@method_decorator(login_required, name='dispatch')
class ReservationDelete(DeleteView):
    model = Reservation
    success_url = reverse_lazy('delete_confirmed')

