# Generated by Django 3.2.18 on 2023-03-01 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tablebooking', '0006_alter_reservation_guest_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='guest_name',
        ),
    ]
