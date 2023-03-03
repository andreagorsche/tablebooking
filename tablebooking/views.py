from django.shortcuts import render

def base(request):
    return render(request, 'tablebooking/base.html')

def booking_form(request):
    return render(request, 'tablebooking/booking_form.html')

def login(request):
    return render(request, 'tablebooking/menu.html')

def manage_booking(request):
    return render(request, 'tablebooking/manage_booking.html')
