# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('p', 'pending'), ('f', 'finished'), ('c', 'closed')], default='p', max_length=1)),
                ('comment', models.TextField()),
            ],
        ),
    ]