from django.conf.urls import include, url
from django.contrib import admin
from People.admin import facultySite
import views

urlpatterns = [
	# url(r'^courselist/', views.FacultyCourseListView.as_view(), name = 'Course List'),
	url(r'^courselist/', facultySite.urls)
]