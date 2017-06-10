# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character_sheet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character_sheet',
            name='class_x',
            field=models.CharField(choices=[('W', 'Wojownik'), ('R', 'Łotrzyk'), ('M', 'Mag'), ('C', 'Kusznik')], default='W', max_length=1),
        ),
        migrations.AddField(
            model_name='character_sheet',
            name='gender',
            field=models.CharField(choices=[('M', 'Mężczyzna'), ('F', 'Kobieta')], default='M', max_length=1),
        ),
        migrations.AddField(
            model_name='character_sheet',
            name='gold',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='character_sheet',
            name='race',
            field=models.CharField(choices=[('H', 'Człowiek'), ('O', 'Ork'), ('E', 'Elf'), ('D', 'Krasnolud')], default='H', max_length=1),
        ),
    ]