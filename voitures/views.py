from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Voiture
# Create your views here.
def car_list(request):
    voitures = Voiture.objects.all()
    return render(request,'voitures/car.html',{'voitures':voitures})
def booking_list(request):
    return render(request,'voitures/detail.html')

def car_detail(request,Matricule):
    # return render(request,'voitures/detail.html')
    voiture = Voiture.objects.get(Matricule=Matricule)
    return render(request, 'voitures/booking.html',{'voiture': voiture })
    # return HttpResponse(Matricule)


    # voiture = Voiture.objects.get(Matricule=Matricule)
    