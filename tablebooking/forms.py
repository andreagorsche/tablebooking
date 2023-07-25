from django import forms
from .models import Reservation, Table
from datetime import datetime
import arrow
from django.core.exceptions import ValidationError

class ReservationForm(forms.ModelForm):
    date = forms.DateField(input_formats=['%d/%m/%Y'])  # Set the input format

    def clean(self):
        cleaned_data = super(ReservationForm, self).clean()
        date = cleaned_data.get('date')

        # Check if the date is in the correct format: dd/mm/yyyy
        try:
            datetime.strptime(str(date), '%Y-%m-%d')
        except ValueError:
            raise forms.ValidationError('Invalid date format. Please use the format DD/MM/YYYY.')

        # Check if the date is in the past
        if date and arrow.utcnow().datetime < date:
            raise forms.ValidationError('You can’t book a table in the past')
        
        return cleaned_data

    class Meta:
        model = Reservation
        fields = ('date', 'time', 'number_of_guests', 'number_of_child_seats', 'comment')



    ''' Attempt to parse the date string into a datetime object
    def clean_date(self):
        date = self.cleaned_data['date']
        try:
            datetime.strptime(date, '%d/%m/%Y')
        except ValueError:
            raise forms.ValidationError("This date is not in the right format. Please use DD/MM/YYYY")
            print("error")
        return date'''