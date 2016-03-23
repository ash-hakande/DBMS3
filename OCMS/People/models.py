from __future__ import unicode_literals

from django.db import models

# Create your models

class Student(models.Model):
	studentID = models.AutoField(primary_key = True)
	firstName = models.CharField('First Name', max_length = 100)
	lastName = models.CharField('Last Name', max_length = 100)
	username = models.CharField('Login Username', max_length = 25)
	password = models.CharField('Login Password', max_length = 20)

	def __str__(self):
		return str(self.firstName+' '+self.lastName)

class Faculty(models.Model):
	facultyID = models.AutoField(primary_key = True)
	firstName = models.CharField('First Name', max_length = 100)
	lastName = models.CharField('Last Name', max_length = 100)
	username = models.CharField('Login Username', max_length = 25)
	password = models.CharField('Login Password', max_length = 20)

	def __str__(self):
		return str(self.firstName+' '+self.lastName)

class Parent(models.Model):
	parentID = models.AutoField(primary_key = True)
	child = models.ForeignKey(Student, on_delete = models.CASCADE, null = True)
	firstName = models.CharField('First Name', max_length = 100)
	lastName = models.CharField('Last Name', max_length = 100)
	username = models.CharField('Login Username', max_length = 25)
	password = models.CharField('Login Password', max_length = 20)

	def __str__(self):
		return str(self.firstName+' '+self.lastName)

class Admin(models.Model):
	adminID = models.AutoField(primary_key = True)
	firstName = models.CharField('First Name', max_length = 100)
	lastName = models.CharField('Last Name', max_length = 100)
	username = models.CharField('Login Username', max_length = 25)
	password = models.CharField('Login Password', max_length = 20)

	def __str__(self):
		return str(self.firstName+' '+self.lastName)

class ParentOf(models.Model):
	studentID = models.ForeignKey(Student, on_delete = models.CASCADE)
	parentID = models.ForeignKey(Parent, on_delete = models.CASCADE)
