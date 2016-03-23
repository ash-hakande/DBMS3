"""OCMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Courses.admin import facultySite
from People.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^', homepage),
    url(r'^student/signup/', studentSignUp, name = 'Student Sign Up'),
    url(r'^student/login/', studentLogin, name = 'Student Login'),
    url(r'^student/home/[0-9]+/', studentMyCourseDisplay, name = 'Student My Course Display'),
    url(r'^student/home/', studentHomePage, name = 'Student Home'),
    url(r'^student/courselist/[0-9]+/', studentCourseDetails, name = 'Student Course Details'),
    url(r'^student/courselist/', studentAllCourseList, name = 'Student All Courses List'),
    url(r'^student/mail/inbox/[0-9]+/', studentMailRecievedBody, name = 'Student Mail Inbox Body'),
    url(r'^student/mail/inbox/', studentMailInbox, name = 'Student Mail Inbox'),
    url(r'^student/mail/sent/[0-9]+/', studentMailSentBody, name = 'Student Mail Sent Body'),
    url(r'^student/mail/sent/', studentMailSent, name = 'Student Mail Sent'),
    url(r'^student/mail/compose/', studentMailCompose, name = 'Student Mail Compose'), 
    url(r'^student/mail/', studentMailHome, name = 'Student Mail Home'),
    url(r'^faculty/signup/', facultySignUp, name = 'Faculty Sign Up'),
    url(r'^faculty/login/', facultyLogin, name = 'Faculty Login'),
    url(r'^faculty/home/', facultyHomePage, name = 'Faculty Home Page'),
    url(r'^parent/signup/', parentSignUp, name = 'Parent Sign Up'),
    url(r'^parent/login/', parentLogin, name = 'Parent Login'),
    url(r'^parent/home/', parentHomePage, name = 'Parent Home Page'),
    url(r'^faculty/mail/inbox/[0-9]+/', facultyMailRecievedBody, name = 'Faculty Mail Inbox Body'),
    url(r'^faculty/mail/inbox/', facultyMailInbox, name = 'Faculty Mail Inbox'),
    url(r'^faculty/mail/sent/[0-9]+/', facultyMailSentBody, name = 'Faculty Mail Sent Body'),
    url(r'^faculty/mail/sent/', facultyMailSent, name = 'Faculty Mail Sent'),
    url(r'^faculty/mail/compose/', facultyMailCompose, name = 'Faculty Mail Compose'), 
    url(r'^faculty/mail/', facultyMailHome, name = 'Faculty Mail Home'), 
    url(r'^faculty/courselist/[0-9]+/assignments/[0-9]+/', facultyViewAssignment, name = "Faculty Course Content"), 
    url(r'^faculty/courselist/[0-9]+/lectures/[0-9]+/', facultyViewLecture, name = "Faculty Course Content"), 
    url(r'^faculty/courselist/[0-9]+/tests/[0-9]+/', facultyViewTest, name = "Faculty Course Content"), 
    url(r'^faculty/courselist/[0-9]+/addassignment/', facultyAddAssignment, name = "Faculty Course Assignment"),
    url(r'^faculty/courselist/[0-9]+/addtest/', facultyAddTest, name = "Faculty Course Test"),
    url(r'^faculty/courselist/[0-9]+/addlecture/', facultyAddLecture, name = "Faculty Course Lecture"),
    url(r'^faculty/courselist/[0-9]+/', facultyCourseContent, name = "Faculty Course Content"), 
]
