from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('date', 'time', 'number_of_people', 'number_of_child_seats', 'comment')
