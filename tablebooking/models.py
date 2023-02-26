from django.db import models
from django.contrib.auth.models import User 

# Create your models here.


class Table (models.Model):
    table_no = models.PositiveIntegerField(unique=True)
    number_of_people = models.PositiveIntegerField()
    private_booth = models.BooleanField(default=False)

class Meta:
    ordering = ['-table_no']


def __str__(self):
    return self.table_no


class Reservation (models.Model):
    reservation_no = models.IntegerField(unique=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    number_of_people = models.PositiveIntegerField()
    number_of_child_seats = models.PositiveIntegerField()


def __str__(self):
    return self.reservation_no

class WaitingList (models.Model):
    rank = models.PositiveIntegerField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)

def __str__(self):
    return self.rank