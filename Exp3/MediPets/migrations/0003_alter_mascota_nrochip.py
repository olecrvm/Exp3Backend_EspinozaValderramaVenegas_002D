# Generated by Django 3.2.3 on 2021-06-18 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MediPets', '0002_alter_mascota_nrochip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='nroChip',
            field=models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='Numero de Chip: '),
        ),
    ]
