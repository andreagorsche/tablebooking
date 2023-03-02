from . import views 
from django.urls import path

urlpatterns = [
    path('', views.base)
    path('booking_form/', views.booking_form)
    path('login/', views.login)
    path('manage_booking/', views.manage_booking)
    path('register/', views.register)

]