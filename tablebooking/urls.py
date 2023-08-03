from . import views
from django.urls import path
from .views import CreateReservation, ReservationList, ReservationUpdate, ReservationDelete

urlpatterns = [
    path('', views.base, name='home'),
    path('create_booking/', CreateReservation.as_view(), name='create_reservation'),
    path('list_booking/', ReservationList.as_view(), name='list_reservation'),
    path('manage_booking/<int:pk>/', ReservationUpdate.as_view(), name='manage_reservation'),
    path('menu/', views.base, name='menu'),
    path('reservation_confirm', views.confirm_reservation, name='confirm_reservation'),
    path('reservation_confirm_delete/<int:pk>/', ReservationDelete.as_view(), name='delete_reservation'),
    path('reservation_confirm_update/', views.confirm_reservation_update, name='conf_upd_reservation'),
    path('delete_confirmed/', views.delete_confirmed, name='delete_confirmed'),
]

handler404 = 'tablebooking.views.error_404'
