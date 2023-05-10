from django.shortcuts import render
from .models import *

def home(request):
    return render(request, 'home.html')

def registration(request):
    return render(request, 'registration.html', {
        'title': 'Registration',
        'headers' : ['Army No', 'Rank', 'Name', 'Appointment', 'Sub Unit', 'Medical Category', 'Age'],
        'data' : Registration.objects.all(),
        
    })

def parade_state(request):
    return render(request, 'parade_state.html')

def bpet_ppt(request):
    return render(request, 'bpet_ppt.html')

def mob_coln(request):
    return render(request, 'mob_coln.html')
    