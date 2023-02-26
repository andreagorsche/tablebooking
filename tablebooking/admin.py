from django.contrib import admin
from .models import Table, Reservation, WaitingList
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Reservation)
class ReservationAdmin(SummernoteModelAdmin):
    
    list_display = ('table', 'date', 'guest_name', 'number_of_people')
    search_fields = ['table', 'guest_name']
    list_filter = ('table','date','number_of_people')
    summernote_fields = ('comment')

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_no', 'number_of_people', 'private_booth')
    search_fields = ['table_no', 'number_of_people', 'private_booth']
    list_filter = ('table_no', 'number_of_people', 'private_booth')   

@admin.register(WaitingList)
class WaitingListAdmin(admin.ModelAdmin):
    list_display = ('table', 'rank', 'reservation')
    search_fields = ['table', 'rank', 'reservation']
    list_filter = ('table', 'rank', 'reservation')  


