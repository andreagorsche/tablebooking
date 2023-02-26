from django.contrib import admin
from .models import Table
from .models import Reservation
from .models import WaitingList

# Register your models here.
admin.site.register(Reservation)
admin.site.register(Table)
admin.site.register(WaitingList)

