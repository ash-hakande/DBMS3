from django.contrib import admin
from models import Course
from People.admin import facultySite

# Register your models here.

facultySite.register(Course)

