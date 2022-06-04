
from django.shortcuts import render
from .models import Directeur
# Create your views here.
def directeurs_list(request):
    directeurs = Directeur.objects.all()
    return render(request,'directeurs/dir.html',{'directeurs':directeurs})
  