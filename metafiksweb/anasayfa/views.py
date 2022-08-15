from django.shortcuts import render
from .models import *
adresler = adres.objects.last()
email_adresi =email_adres.objects.last()
logo = sayfa_logosu.objects.last()
numaras = numara.objects.last() 
facebook= sosyalmedyafb.objects.last()
insta = sosyalmedyaInsgr.objects.last()
twit = sosyalmedyaTw.objects.last()
linkdin = sosyalmedyalinkd.objects.last()
# Create your views here.
def anasayfa(request):
    ban = banner.objects.all()[:3]
    content = {"adresler":adresler,"email_adresi":email_adresi,
    "logo":logo,"numara":numaras,"facebook":facebook,"insta":insta,
    "twit":twit,"linkdin":linkdin,"ban":ban}

    return render(request,"home_temps/index.html",content)