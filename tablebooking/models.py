from django.db import models
from django.contrib.auth.models import User


class Table (models.Model):
    table_no = models.PositiveIntegerField(unique=True)
    number_of_seats = models.PositiveIntegerField()
    private_booth = models.BooleanField(default=False)


class Meta:
    ordering = ['-table_no']


def __str__(self):
    return self.table_no


class Reservation (models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    date = models.DateField()
    time = models.TimeField()
    number_of_guests = models.PositiveIntegerField()
    number_of_child_seats = models.PositiveIntegerField()
    comment = models.TextField(blank=True)
    is_waitlisted = models.BooleanField(default=False)


def __str__(self):
    return self.table
