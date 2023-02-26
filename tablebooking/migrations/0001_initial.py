# Generated by Django 3.2.18 on 2023-02-26 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_no', models.PositiveIntegerField(unique=True)),
                ('number_of_people', models.PositiveIntegerField()),
                ('private_booth', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_no', models.IntegerField(unique=True)),
                ('guest_name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('number_of_people', models.PositiveIntegerField()),
                ('number_of_child_seats', models.PositiveIntegerField()),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tablebooking.table')),
            ],
        ),
    ]
