from __future__ import unicode_literals

from django.db import models
from People import Faculty

# Create your models here.

class Course(models.Model):
	courseID = models.AutoField(primary_key = True)
	courseName = models.CharField('Course Name', max_length = 50)
	courseField = models.CharField('Course Field', max_length = 50)
	faculties = models.ManyToManyField(Faculty)
