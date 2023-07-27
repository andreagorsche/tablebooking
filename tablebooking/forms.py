from django import forms
from .models import Reservation, Table
from datetime import datetime
import arrow
from django.core.exceptions import ValidationError

class ReservationForm(forms.ModelForm):
    # Check if the date is in the correct format: dd/mm/yyyy
    date = forms.DateField(
        input_formats=["%d/%m/%Y"],
        error_messages={
            "invalid": "Please enter a valid date in the format DD/MM/YYYY."
        },
    )
    # Check if the time is in the correct format: hh:mm
    time = forms.TimeField(
        error_messages={"invalid": "Please enter a valid time in the format HH:MM."}
    )
    class Meta:
        model = Reservation
        fields = (
            "date",
            "time",
            "number_of_guests",
            "number_of_child_seats",
            "comment",
        )
    def clean(self):
        cleaned_data = super(ReservationForm, self).clean()
        date = cleaned_data.get("date")
        number_of_guests = cleaned_data.get("number_of_guests")
        # Check if the date is in the past
        if date and date < date.today():
            raise forms.ValidationError("You can't book a table in the past")
        # Check if number_of_guests are not None and not small or equal to null
        if number_of_guests is not None and number_of_guests <= 0:
            raise forms.ValidationError("Number of guests must be greater than 0.")
        return cleaned_data