# Generated by Django 4.2.4 on 2023-09-10 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busArrivalTime', '0005_arrivaltimes_deviceid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='arrivaltimes',
            old_name='latitute',
            new_name='latitude',
        ),
    ]
