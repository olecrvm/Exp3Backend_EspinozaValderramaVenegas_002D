# Generated by Django 3.2.4 on 2021-06-18 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MediPets', '0003_alter_mascota_nrochip'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mascota',
            old_name='nroChip',
            new_name='nrochip',
        ),
    ]
