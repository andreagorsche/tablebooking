from django.db import models
from django.contrib.auth.models import User 


class Table (models.Model):
    table_no = models.PositiveIntegerField(unique=True)
    number_of_people = models.PositiveIntegerField()
    private_booth = models.BooleanField(default=False)

class Meta:
    ordering = ['-table_no']


def __str__(self):
    return self.table_no

class Reservation (models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    number_of_people = models.PositiveIntegerField()
    number_of_child_seats = models.PositiveIntegerField()
    comment = models.TextField(blank=True)
    is_waitlisted = models.BooleanField(default=False)

class Guest (models.Model):
    first_name = models.CharField(max_length= 25)
    last_name = models.CharField(max_length= 25)
    username = models.CharField(max_length= 50)
    email = models. EmailField()
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)

