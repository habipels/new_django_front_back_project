from django.shortcuts import render

from egitimler.models import egitimler
from .models import *
adresler = adres.objects.last()
email_adresi =email_adres.objects.last()
logo = sayfa_logosu.objects.last()
numaras = numara.objects.last() 
facebook= sosyalmedyafb.objects.last()
insta = sosyalmedyaInsgr.objects.last()
twit = sosyalmedyaTw.objects.last()
linkdin = sosyalmedyalinkd.objects.last()
egitimleri = egitimler.objects.all()
# Create your views here.
def anasayfa(request):
    ban = banner.objects.all()[:3]
    content = {"adresler":adresler,"email_adresi":email_adresi,
    "logo":logo,"numara":numaras,"facebook":facebook,"insta":insta,
    "twit":twit,"linkdin":linkdin,"ban":ban,"egitimleri":egitimleri}

    return render(request,"home_temps/index.html",content)

def anasayfa(request):

    content = {"adresler":adresler,"email_adresi":email_adresi,
    "logo":logo,"numara":numaras,"facebook":facebook,"insta":insta,
    "twit":twit,"linkdin":linkdin,"egitimleri":egitimleri}

    return render(request,"egitimler_temps/index.html",content)