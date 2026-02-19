from django.http import HttpResponse
from django.shortcuts import render

from .forms import BookingForm
from .models import Departments, Mechanic, Booking


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def booking(request):
    if request.method=="POST":
        form =BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form= BookingForm()
    dict_form={
        'form': form
    }
    return render(request,'booking.html',dict_form)

def mechanics(request):
    dict_mech={
        'Mechanics':Mechanic.objects.all()
    }
    return render(request,'mechanics.html',dict_mech)

def contact(request):
    return render(request,'contact.html')


def department(request):
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request,'department.html',dict_dept)