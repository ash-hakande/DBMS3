from django import forms
from django.forms.models import inlineformset_factory, modelformset_factory
from django.forms.formsets import BaseFormSet
from .models import *
from Courses.models import *
from Mail.models import *

class StudentSignUpForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ['firstName', 'lastName', 'username', 'password']

class StudentLoginForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ['username', 'password']

class FacultySignUpForm(forms.ModelForm):
	class Meta:
		model = Faculty
		fields = ['firstName', 'lastName', 'username', 'password']

class FacultyLoginForm(forms.ModelForm):
	class Meta:
		model = Faculty
		fields = ['username', 'password']

class ParentSignUpForm(forms.Form):
	firstName = forms.CharField(label = 'firstName')
	lastName = forms.CharField(label = 'lastName')
	child = forms.CharField(label = 'child')
	username = forms.CharField(label = 'username')
	password = forms.CharField(label = 'password')

class ParentLoginForm(forms.ModelForm):
	class Meta:
		model = Parent
		fields = ['username', 'password']

class StudentMailComposeForm(forms.Form):
	facultyName = forms.CharField(label='Faculty name')
	mailSubject = forms.CharField(label='Mail Subject')
	mailText = forms.CharField(label='Mail Body') 

class StudentMailComposeForm(forms.Form):
	facultyName = forms.CharField(label='Faculty name')
	mailSubject = forms.CharField(label='Mail Subject')
	mailText = forms.CharField(label='Mail Body') 

class TestTake(forms.Form):
	choice1 = forms.CharField(label = 'choice1')
	choice2 = forms.CharField(label = 'choice2')
	choice3 = forms.CharField(label = 'choice3')
	choice4 = forms.CharField(label = 'choice4')
	choice5 = forms.CharField(label = 'choice5')
	choice6 = forms.CharField(label = 'choice6')
	choice7 = forms.CharField(label = 'choice7')
	choice8 = forms.CharField(label = 'choice8')
	choice9 = forms.CharField(label = 'choice9')
	choice10 = forms.CharField(label = 'choice10')

# def facultyAddAssignmentForm(forms.ModelForm):
# 	class Meta:
# 		model = Assignment
# 		fields = ['assignmentTitle', 'assignmentText']

# def facultyAddLectureForm(forms.ModelForm):
# 	class Meta:
# 		model = Lecture
# 		fields = ['lectureTitle', 'lectureText', 'lectureWeek']

class FacultyAddTestForm(forms.Form):
	question1 = forms.CharField(label = 'Question1')
	question2 = forms.CharField(label = 'Question2')
	question3 = forms.CharField(label = 'Question3')
	question4 = forms.CharField(label = 'Question4')
	question5 = forms.CharField(label = 'Question5')
	question1option1 = forms.CharField(label = 'Question1Option1')
	question1option2 = forms.CharField(label = 'Question1Option2')
	question1option3 = forms.CharField(label = 'Question1Option3')
	question1option4 = forms.CharField(label = 'Question1Option4')
	question1answer = forms.CharField(label = 'Question1Answer')
	question2option1 = forms.CharField(label = 'Question2Option1')
	question2option2 = forms.CharField(label = 'Question2Option2')
	question2option3 = forms.CharField(label = 'Question2Option3')
	question2option4 = forms.CharField(label = 'Question2Option4')
	question2answer = forms.CharField(label = 'Question2Answer')
	question3option1 = forms.CharField(label = 'Question3Option1')
	question3option2 = forms.CharField(label = 'Question3Option2')
	question3option3 = forms.CharField(label = 'Question3Option3')
	question3option4 = forms.CharField(label = 'Question3Option4')
	question3answer = forms.CharField(label = 'Question3Answer')
	question4option1 = forms.CharField(label = 'Question4Option1')
	question4option2 = forms.CharField(label = 'Question4Option2')
	question4option3 = forms.CharField(label = 'Question4Option3')
	question4option4 = forms.CharField(label = 'Question4Option4')
	question4answer = forms.CharField(label = 'Question4Answer')
	question5option1 = forms.CharField(label = 'Question5Option1')
	question5option2 = forms.CharField(label = 'Question5Option2')
	question5option3 = forms.CharField(label = 'Question5Option3')
	question5option4 = forms.CharField(label = 'Question5Option4')
	question5answer = forms.CharField(label = 'Question5Answer')

