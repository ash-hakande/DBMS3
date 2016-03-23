from django.contrib import admin
from models import Course, Registered
from People.admin import facultySite

# Register your models here.

facultySite.register(Course)

admin.site.register(Course)
admin.site.register(Registered)

