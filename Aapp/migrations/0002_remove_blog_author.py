# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-23 09:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
    ]
