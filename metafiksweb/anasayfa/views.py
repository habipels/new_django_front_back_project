from django.shortcuts import render
from .models import *
adresler = adres.objects.last()
email_adresi =email_adres.objects.last()
logo = sayfa_logosu.objects.last()
numaras = numara.objects.last() 
# Create your views here.
def anasayfa(request):
    content = {"adresler":adresler,"email_adresi":email_adresi,"logo":logo,"numara":numaras}
    return render(request,"home_temps/index.html",content)