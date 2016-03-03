from __future__ import unicode_literals

from django.db import models
from Courses.models import Course
from People.models import Student

# Create your models here.

class Question(models.Model):
	questionID = models.AutoField(primary_key = True)
	questionText = models.CharField('Question', max_length = 100)
	choice1 = models.CharField('Choice 1', max_length = 50)
	choice2 = models.CharField('Choice 2', max_length = 50)
	choice3 = models.CharField('Choice 3', max_length = 50)
	choice4 = models.CharField('Choice 4', max_length = 50)
	questionMarks = models.IntegerField('Question Marks')

class Test(models.Model):
	testID = models.AutoField(primary_key = True)
	testTitle = models.CharField('Title', max_length = 50)
	questions = models.ManyToManyField(Question)

class Assignment(models.Model):
	assignmentID = models.AutoField(primary_key = True)
	assignmentTitle = models.CharField('Title', max_length = 50)
	assignmentText = models.CharField('Assignment', max_length = 500)

class Lecture(models.Model):
	lectureID = models.AutoField(primary_key = True)
	lectureTitle = models.CharField('Title', max_length = 50)
	lectureText = models.CharField('Lecture', max_length = 500)

class CourseContent(models.Model):
	courseID = models.ForeignKey(Course)
	lectures = models.ManyToManyField(Lecture)
	assignments = models.ManyToManyField(Assignment)
	tests = models.ManyToManyField(Test)

class Evaluation(models.Model):
	studentID = models.ForeignKey(Student)
	testID = models.ForeignKey(Test)
	marks = models.IntegerField('Marks Obtained')

