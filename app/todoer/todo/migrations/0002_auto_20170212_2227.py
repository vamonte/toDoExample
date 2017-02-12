# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 22:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='comment',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('finished', 'finished'), ('closed', 'closed')], default='pending', max_length=10),
        ),
    ]
