# Generated by Django 2.1.4 on 2019-03-20 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PowerZoneAPI', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='presa',
            old_name='tipo',
            new_name='presa',
        ),
    ]