# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-16 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CourseMatter', '0002_lecture_lectureweek'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='questionMarks',
        ),
        migrations.AddField(
            model_name='question',
            name='correct',
            field=models.CharField(max_length=1, null=True, verbose_name='Correct Answer'),
        ),
        migrations.AlterField(
            model_name='question',
            name='choice1',
            field=models.CharField(max_length=50, null=True, verbose_name='Choice 1'),
        ),
        migrations.AlterField(
            model_name='question',
            name='choice2',
            field=models.CharField(max_length=50, null=True, verbose_name='Choice 2'),
        ),
        migrations.AlterField(
            model_name='question',
            name='choice3',
            field=models.CharField(max_length=50, null=True, verbose_name='Choice 3'),
        ),
        migrations.AlterField(
            model_name='question',
            name='choice4',
            field=models.CharField(max_length=50, null=True, verbose_name='Choice 4'),
        ),
        migrations.AlterField(
            model_name='question',
            name='questionText',
            field=models.CharField(max_length=100, null=True, verbose_name='Question'),
        ),
    ]
