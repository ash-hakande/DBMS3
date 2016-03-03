from __future__ import unicode_literals

from django.db import models

# Create your models here.

class StudentToFacultyMail(models.Model):
	studentID = models.ForeignKey(Student, on_delete = models.CASCADE)
	facultyID = models.ForeignKey(Faculty, on_delete = models.CASCADE)
	mailText = models.CharField('Mail Body', max_length = 500) 

class ParentToFacultyMail(models.Model):
	parentID = models.ForeignKey(Parent, on_delete = models.CASCADE)
	facultyID = models.ForeignKey(Faculty, on_delete = models.CASCADE)
	mailText = models.CharField('Mail Body', max_length = 500) 

class FacultyToStudentMail(models.Model):
	facultyID = models.ForeignKey(Faculty, on_delete = models.CASCADE)
	studentID = models.ForeignKey(Student, on_delete = models.CASCADE)
	mailText = models.CharField('Mail Body', max_length = 500) 

class FacultyToParentMail(models.Model):
	facultyID = models.ForeignKey(Faculty, on_delete = models.CASCADE)
	parententID = models.ForeignKey(Parent, on_delete = models.CASCADE)
	mailText = models.CharField('Mail Body', max_length = 500) 
