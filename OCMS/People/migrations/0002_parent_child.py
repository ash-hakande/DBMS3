# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-10 10:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('People', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='child',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='People.Student'),
        ),
    ]
