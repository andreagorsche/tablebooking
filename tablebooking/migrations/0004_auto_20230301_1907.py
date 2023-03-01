# Generated by Django 3.2.18 on 2023-03-01 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablebooking', '0003_reservation_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='reservation_no',
        ),
        migrations.AddField(
            model_name='reservation',
            name='is_waitlisted',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='WaitingList',
        ),
    ]
