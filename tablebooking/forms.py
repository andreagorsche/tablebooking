from django import forms
from .models import Reservation, Table
from datetime import datetime

class ReservationForm(forms.ModelForm):
    date = forms.DateField(input_formats=['%d/%m/%Y'])  # Set the input format

    class Meta:
        model = Reservation
        fields = ('date', 'time', 'number_of_guests', 'number_of_child_seats', 'comment')

    # Attempt to parse the date string into a datetime object
    def clean_date(self):
        date = self.cleaned_data['date']
        try:
            datetime.strptime(date, '%d/%m/%Y')
        except ValueError:
            raise forms.ValidationError("This date is not in the right format. Please use DD/MM/YYYY")
            print("error")
        return date