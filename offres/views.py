from django.shortcuts import render

# Create your views here.
from .models import Offre
# Create your views here.
def offre_list(request):
    offres = Offre.objects.all()
    return render(request,'offres/detail.html',{'offres':offres})
    # ,{'offres':offres}