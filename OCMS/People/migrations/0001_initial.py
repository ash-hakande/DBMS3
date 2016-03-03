# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-03 01:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('adminID', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=100, verbose_name='First Name')),
                ('lastName', models.CharField(max_length=100, verbose_name='Last Name')),
                ('username', models.CharField(max_length=25, verbose_name='Login Username')),
                ('password', models.CharField(max_length=20, verbose_name='Login Password')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('facultyID', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=100, verbose_name='First Name')),
                ('lastName', models.CharField(max_length=100, verbose_name='Last Name')),
                ('username', models.CharField(max_length=25, verbose_name='Login Username')),
                ('password', models.CharField(max_length=20, verbose_name='Login Password')),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('parentID', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=100, verbose_name='First Name')),
                ('lastName', models.CharField(max_length=100, verbose_name='Last Name')),
                ('username', models.CharField(max_length=25, verbose_name='Login Username')),
                ('password', models.CharField(max_length=20, verbose_name='Login Password')),
            ],
        ),
        migrations.CreateModel(
            name='ParentOf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='People.Parent')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentID', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=100, verbose_name='First Name')),
                ('lastName', models.CharField(max_length=100, verbose_name='Last Name')),
                ('username', models.CharField(max_length=25, verbose_name='Login Username')),
                ('password', models.CharField(max_length=20, verbose_name='Login Password')),
            ],
        ),
        migrations.AddField(
            model_name='parentof',
            name='studentID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='People.Student'),
        ),
    ]