from . import views
from django.urls import path
from .views import create_booking

urlpatterns = [
    path('', views.base, name='home'),
#   path('booking_form/', views.booking_form, name='booking_form'),
    path('create_booking/', create_booking.as_view(), name='create_booking'),
    path('menu/', views.login, name='menu'),
    path('manage_booking/', views.manage_booking, name='manage_booking'),
]
