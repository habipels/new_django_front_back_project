from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(sayfa_logosu)
admin.site.register(numara)
admin.site.register(adres)
admin.site.register(email_adres)