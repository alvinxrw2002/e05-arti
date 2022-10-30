# Generated by Django 4.1 on 2022-10-30 08:07
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arti', '0007_karya_kategori'),
    ]

    def generate_superuser(apps, schema_editor):
        from django.contrib.auth.models import User

        superuser = User.objects.create_superuser(
            username='admin',
            email='admin@admin.com',
            password='admin123')

        superuser.save()

    operations = [
        migrations.RunPython(generate_superuser),
    ]
