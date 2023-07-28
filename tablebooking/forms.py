from django import forms
from .models import Reservation, Table
from datetime import date, time as time_lib
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
        time = cleaned_data.get("time")
        comment = cleaned_data.get("comment")
        number_of_guests = cleaned_data.get("number_of_guests")

        # Check if the date is in the past
        if date and date < date.today():
            raise forms.ValidationError("You can't book a table in the past")

        # Check if the date is not a Monday (weekday number 0)
        if date and date.weekday() == 0:
            raise forms.ValidationError('The restaurant is closed on Mondays. Please select a different date.')

        # Check if number_of_guests are not None and not small or equal to null
        if number_of_guests is not None and number_of_guests <= 0:
            raise forms.ValidationError("Number of guests must be greater than 0.")
       

        # Check if the time is between opening times (10 am to 8 pm)
        opening_time = time_lib(10, 0)  # 10:00 AM
        closing_time = time_lib(20, 0)  # 8:00 PM
        if time and (time < opening_time or time > closing_time):
            raise forms.ValidationError('The restaurant is open from 10:00 AM to 8:00 PM. Please select a valid time.')
        
        # Check if the comment is not more than 300 characters
        if comment and len(comment) > 300:
            raise forms.ValidationError('Comment must not exceed 300 characters.')
         
        return cleaned_data