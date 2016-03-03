from __future__ import unicode_literals

from django.db import models
from People.models import Student, Faculty, Parent

# Create your models here.

class StudentToFacultyMail(models.Model):
	studentID = models.ForeignKey(Student, on_delete = models.CASCADE)
	facultyID = models.ForeignKey(Faculty, on_delete = models.CASCADE)
	mailSubject = models.CharField('Mail Subject', max_length = 50)
	mailText = models.CharField('Mail Body', max_length = 500) 

	def __str__(self):
		return str(self.mailSubject)

class ParentToFacultyMail(models.Model):
	parentID = models.ForeignKey(Parent, on_delete = models.CASCADE)
	facultyID = models.ForeignKey(Faculty, on_delete = models.CASCADE)
	mailSubject = models.CharField('Mail Subject', max_length = 50)
	mailText = models.CharField('Mail Body', max_length = 500) 

	def __str__(self):
		return str(self.mailSubject)

class FacultyToStudentMail(models.Model):
	facultyID = models.ForeignKey(Faculty, on_delete = models.CASCADE)
	studentID = models.ForeignKey(Student, on_delete = models.CASCADE)
	mailSubject = models.CharField('Mail Subject', max_length = 50)
	mailText = models.CharField('Mail Body', max_length = 500) 

	def __str__(self):
		return str(self.mailSubject)

class FacultyToParentMail(models.Model):
	facultyID = models.ForeignKey(Faculty, on_delete = models.CASCADE)
	parententID = models.ForeignKey(Parent, on_delete = models.CASCADE)
	mailSubject = models.CharField('Mail Subject', max_length = 50)
	mailText = models.CharField('Mail Body', max_length = 500) 

	def __str__(self):
		return str(self.mailSubject)
