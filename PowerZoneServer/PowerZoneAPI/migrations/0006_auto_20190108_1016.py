# Generated by Django 2.1.4 on 2019-01-08 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PowerZoneAPI', '0005_auto_20190108_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recensione',
            name='voto',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]