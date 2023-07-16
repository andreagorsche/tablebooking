from . import views
from django.urls import path
from .views import CreateReservation, ReservationList

urlpatterns = [
    path('', views.base, name='home'),
#   path('booking_form/', views.booking_form, name='booking_form'),
    path('create_booking/', CreateReservation.as_view(), name='create_reservation'),
    path('list_booking/', ReservationList.as_view(), name='list_reservation'),
    path('menu/', views.login, name='menu'),
]
