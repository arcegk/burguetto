# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-28 05:20
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=40)),
                ('selections', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
