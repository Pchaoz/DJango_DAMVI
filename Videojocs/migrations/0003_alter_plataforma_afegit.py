# Generated by Django 4.1.7 on 2023-02-28 23:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Videojocs', '0002_videojoc_usuaris_alter_plataforma_afegit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plataforma',
            name='afegit',
            field=models.DateField(default=datetime.datetime(2023, 2, 28, 23, 5, 52, 838125, tzinfo=datetime.timezone.utc)),
        ),
    ]
