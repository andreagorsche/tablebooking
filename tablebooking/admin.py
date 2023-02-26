from django.contrib import admin
from .models import Table
from .models import Reservation
from .models import WaitingList
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Reservation)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('comment')

# Register your models here.
admin.site.register(Table)
admin.site.register(WaitingList)

