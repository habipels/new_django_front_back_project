from statistics import mode
from django.db import models

# Create your models here.
class sayfa_logosu(models.Model):
    sayfa_logo = models.FileField(upload_to='logo/',blank = True,null = True,verbose_name="Sayfaya Logo Ekleyin")

class numara(models.Model):
    sirket_numarasi = models.CharField(max_length=11)
class adres(models.Model):
    sirket_adresi = models.CharField(max_length=200)

class email_adres(models.Model):
    sirket_email_adresi = models.EmailField(max_length=200)

class sosyalmedyaTw(models.Model):
    link = models.CharField(max_length=400)

class sosyalmedyafb(models.Model):
    link = models.CharField(max_length=400)

class sosyalmedyaInsgr(models.Model):
    link = models.CharField(max_length=400)

class sosyalmedyalinkd(models.Model):
    link = models.CharField(max_length=400)

class banner(models.Model):
    sayfa_sirasi = models.BigIntegerField(null=True)
    baner_resim = models.FileField(upload_to='banner/',blank = True,verbose_name="Sayfaya resim Ekleyiniz")