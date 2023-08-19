from django.db import models
from django.contrib.auth.models import User


class Table (models.Model):
    """
    Model defining the restaurant table and its fields.
    Asigning a table number, the number of possible seats
    and the option to set the table up as a private booth
    on customer request.
    """
    table_no = models.PositiveIntegerField(unique=True)
    number_of_seats = models.PositiveIntegerField()
    private_booth = models.BooleanField(default=False)

    class Meta:
        """
        Meta class defining that tables should be ordered in descending order
        """
        ordering = ['-table_no']

    def __str__(self):
        """
        String method returning the table number
        """
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
        """
        String method returning the table
        """
        return self.table
