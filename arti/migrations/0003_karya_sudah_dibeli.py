# Generated by Django 4.1 on 2022-11-01 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arti', '0002_alter_karya_deskripsi_alter_karya_harga'),
    ]

    operations = [
        migrations.AddField(
            model_name='karya',
            name='sudah_dibeli',
            field=models.BooleanField(default=False),
        ),
    ]
