from django.db import models

# Create your models here.
class sayfa_logosu(models.Model):
    sayfa_logo = models.FileField(upload_to='logo/',blank = True,null = True,verbose_name="Sayfaya Logo Ekleyin")