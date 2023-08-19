from django.contrib import admin
from .models import Table, Reservation
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Reservation)
class ReservationAdmin(SummernoteModelAdmin):
    """
    This class defines the reservation display,
    search fields and filter for the admin site
    and it defines that the comment field is
    displayed in the summernote look
    """
    list_display = ('table', 'date', 'number_of_guests', 'is_waitlisted')
    search_fields = ['table']
    list_filter = ('table', 'date', 'number_of_guests', 'is_waitlisted')
    summernote_fields = ('comment')


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    """
    This class defines the table display,
    search fields and filter for the admin site
    """
    list_display = ('table_no', 'number_of_seats', 'private_booth')
    search_fields = ['table_no', 'number_of_seats', 'private_booth']
    list_filter = ('table_no', 'number_of_seats', 'private_booth')
