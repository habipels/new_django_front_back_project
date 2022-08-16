from django.db import models
from ckeditor_uploader.fields import  RichTextUploadingField
class kategoriler(models.Model):
    isim = models.CharField(max_length=50)
    link = models.CharField(max_length=100 , null="True")
    keywords = models.CharField(max_length=255) 
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE)
    def __str__(self):
        full_path = [self.isim]                  # post.  use __unicode__ in place of
        k = self.parent
        while k is not None:
            full_path.append(k.isim)
            k = k.parent
        return ' --> '.join(full_path[::-1])
# Create your models here.
class egitimler(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    kapak_image=models.ImageField(upload_to='images/',null=True)
    category = models.ForeignKey(kategoriler, on_delete=models.CASCADE)
    isim = models.CharField(max_length=150)
    link = models.CharField(max_length=100 , null="True")
    odeme_linki = models.CharField(max_length=255 , null="True")
    keywords = models.CharField(max_length=255)
    aciklama_kart1 = models.CharField(max_length=100)
    aciklama_kart2 = models.CharField(max_length=100)
    aciklama_kart3 = models.CharField(max_length=100)
    aciklama_kart4 = models.CharField(max_length=100)
    aciklama_kart5 = models.CharField(max_length=100)
    egitim_gunleri = models.CharField(max_length=250)
    image=models.ImageField(upload_to='images/',null=False)
    fiyat = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    kontejan=models.IntegerField(default=0)
    urun_sag_metin=RichTextUploadingField()
    Durum=models.CharField(max_length=10,choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    toplam_egitim_saati =models.CharField(max_length=50)
    egitim_tarihi=models.DateTimeField()
    egitim_bitis_tarihi = models.DateTimeField()
    urun_aciklama=RichTextUploadingField()
    urun_mufredat=RichTextUploadingField()
    urun_tarih_ucret=RichTextUploadingField()
    urun_sertifikalar=RichTextUploadingField()
    def __str__(self):
        return self.isim

class kurlar(models.Model):
    kur_Adi = models.CharField(max_length= 100)


class kurlar_secimi(models.Model):
    kur_Adi = models.ForeignKey(kurlar, on_delete=models.CASCADE)
    ders = models.ForeignKey(egitimler, on_delete=models.CASCADE)
    egitim_tarihi=models.DateTimeField()