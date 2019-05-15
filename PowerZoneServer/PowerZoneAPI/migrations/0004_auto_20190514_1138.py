# Generated by Django 2.1.4 on 2019-05-14 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PowerZoneAPI', '0003_auto_20190413_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presa',
            name='presa',
            field=models.CharField(choices=[('PREL', 'Presa elettrica'), ('PUSB', 'Presa USB'), ('PRAU', 'Presa auto elettrica')], default='PREL', max_length=4),
        ),
    ]