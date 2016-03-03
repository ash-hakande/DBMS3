from __future__ import unicode_literals

from django.db import models
from People.models import Student, Faculty
# from CourseMatter.models import Test

# Create your models here.

class Course(models.Model):
	courseID = models.AutoField(primary_key = True)
	courseName = models.CharField('Course Name', max_length = 50)
	courseField = models.CharField('Course Field', max_length = 50)
	faculties = models.ManyToManyField(Faculty)
	prerequisites = models.CharField('Pre-requisites', max_length = 200)

	def __str__(self):
		return str(self.courseName)

class Registered(models.Model):
	studentID = models.ForeignKey(Student)
	courseID = models.ForeignKey(Course)

