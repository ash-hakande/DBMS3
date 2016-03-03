from django.shortcuts import render
from People.models import Faculty
from models import Course
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required, user_passes_test
import os

def isFaculty(user):
	return Faculty.objects.filter(username__exact=user.username).exists()

# Create your views here.

print os.getcwd()

class FacultyCourseListView(ListView):

	context_object_name = 'faculty_course_list'
	template_name = '/Course_List.html'
	
	def get_queryset(self):
		allCourses = Course.objects.all()
		querySet=[]
		for course in allCourses:
			faculties = course.faculties
			present = False
			for faculty in faculties :
				if current_faculty.facultyID==faculty.facultyID:
					present = True
					break
			if present : querySet.append(course)
		return querySet

	def get_response(self):
		return super.get_response()
