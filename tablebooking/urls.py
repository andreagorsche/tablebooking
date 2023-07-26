from . import views
from django.urls import path
from .views import CreateReservation, ReservationList, ReservationUpdate, ReservationDelete

urlpatterns = [
    path('', views.base, name='home'),
#   path('booking_form/', views.booking_form, name='booking_form'),
    path('create_booking/', CreateReservation.as_view(), name='create_reservation'),
    path('list_booking/', ReservationList.as_view(), name='list_reservation'),
    path('manage_booking/<int:pk>/', ReservationUpdate.as_view(), name='manage_reservation'),
    path('confirm_delete/<int:pk>/', ReservationDelete.as_view(), name='delete_reservation'),
    path('confirm_update/<int:pk>/', ReservationUpdate.as_view(), name='upd_conf_reservation'),
    path('menu/', views.login, name='menu'),
]
