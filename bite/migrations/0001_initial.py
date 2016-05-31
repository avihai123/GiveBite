# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 10:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=200)),
                ('dish_price', models.DecimalField(decimal_places=2, max_digits=14)),
                ('dish_desc', models.CharField(max_length=1000)),
            ],
        ),
    ]