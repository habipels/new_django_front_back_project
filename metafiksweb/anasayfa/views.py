from django.shortcuts import render

from egitimler.models import *
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
    kurlarrim = kurlar.objects.all()
    ban = banner.objects.all()[:3]
    content = {"adresler":adresler,"email_adresi":email_adresi,
    "logo":logo,"numara":numaras,"facebook":facebook,"insta":insta,
    "twit":twit,"linkdin":linkdin,"ban":ban,"egitimleri":egitimleri,"kurlarrim":kurlarrim}

    return render(request,"home_temps/index.html",content)

def egitimler(request):
    kurlarrim = kurlar.objects.all()
    content = {"adresler":adresler,"email_adresi":email_adresi,
    "logo":logo,"numara":numaras,"facebook":facebook,"insta":insta,
    "twit":twit,"linkdin":linkdin,"egitimleri":egitimleri,"kurlarrim":kurlarrim}

    return render(request,"egitimler_temps/index.html",content)

def egitimler_secimi(request,id):
    kurlarrim = kurlar.objects.all()
    kur = kurlar_secimi.objects.filter(kur_Adi = id).order_by("egitim_tarihi")
    content = {"adresler":adresler,"email_adresi":email_adresi,
    "logo":logo,"numara":numaras,"facebook":facebook,"insta":insta,
    "twit":twit,"linkdin":linkdin,"egitimleri":egitimleri,"kurlarrim":kurlarrim,"kur":kur}

    return render(request,"egitimler_temps/index.html",content)

def hakkimizda(request):
    kurlarrim = kurlar.objects.all()
    ban = banner.objects.all()[:3]
    hakimda = hakkimizda_sayfasi.objects.last()
    content = {"adresler":adresler,"email_adresi":email_adresi,
    "logo":logo,"numara":numaras,"facebook":facebook,"insta":insta,
    "twit":twit,"linkdin":linkdin,"ban":ban,"egitimleri":egitimleri,"kurlarrim":kurlarrim,"hakimda":hakimda}

    return render(request,"hakkimizda_temps/index.html",content)

def iletisim(request):
    kurlarrim = kurlar.objects.all()
    ban = banner.objects.all()[:3]
    content = {"adresler":adresler,"email_adresi":email_adresi,
    "logo":logo,"numara":numaras,"facebook":facebook,"insta":insta,
    "twit":twit,"linkdin":linkdin,"ban":ban,"egitimleri":egitimleri,"kurlarrim":kurlarrim}

    return render(request,"iletisim_temps/index.html",content)