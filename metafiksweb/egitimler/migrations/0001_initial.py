# Generated by Django 3.2.13 on 2022-08-15 13:26

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='kategoriler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=100, null='True')),
                ('keywords', models.CharField(max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='egitimler.kategoriler')),
            ],
        ),
        migrations.CreateModel(
            name='egitimler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=150)),
                ('link', models.CharField(max_length=100, null='True')),
                ('odeme_linki', models.CharField(max_length=255, null='True')),
                ('keywords', models.CharField(max_length=255)),
                ('aciklama_kart1', models.CharField(max_length=100)),
                ('aciklama_kart2', models.CharField(max_length=100)),
                ('aciklama_kart3', models.CharField(max_length=100)),
                ('aciklama_kart4', models.CharField(max_length=100)),
                ('aciklama_kart5', models.CharField(max_length=100)),
                ('egitim_gunleri', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='images/')),
                ('fiyat', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('kontejan', models.IntegerField(default=0)),
                ('urun_sag_metin', ckeditor_uploader.fields.RichTextUploadingField()),
                ('Durum', models.CharField(choices=[('True', 'Evet'), ('False', 'Hay??r')], max_length=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('toplam_egitim_saati', models.CharField(max_length=50)),
                ('egitim_tarihi', models.DateTimeField()),
                ('egitim_bitis_tarihi', models.DateTimeField()),
                ('urun_aciklama', ckeditor_uploader.fields.RichTextUploadingField()),
                ('urun_mufredat', ckeditor_uploader.fields.RichTextUploadingField()),
                ('urun_tarih_ucret', ckeditor_uploader.fields.RichTextUploadingField()),
                ('urun_sertifikalar', ckeditor_uploader.fields.RichTextUploadingField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='egitimler.kategoriler')),
            ],
        ),
    ]
