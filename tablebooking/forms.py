from django import forms
from .models import Reservation, Table

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('date', 'time', 'number_of_guests', 'number_of_child_seats', 'comment')

'''     def clean_date(self):
        date = self.cleaned_data['date']
        try:
            validated_date = validate_date(date)
        except ValidationError as e:
            raise forms.ValidationError(e.message)

        return validated_date'''



