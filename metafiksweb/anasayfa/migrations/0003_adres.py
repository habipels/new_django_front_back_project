# Generated by Django 3.2.13 on 2022-08-15 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0002_numara'),
    ]

    operations = [
        migrations.CreateModel(
            name='adres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sirket_adresi', models.CharField(max_length=200)),
            ],
        ),
    ]
