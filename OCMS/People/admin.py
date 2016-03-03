from django.contrib import admin
from models import Student, Faculty, Parent, Admin

# Register your models here.

class StudentSite(admin.AdminSite):
	site_header = 'Welcome Student!'

class FacultySite(admin.AdminSite):
	site_header = 'Welcome Faculty!'

admin.site.register(Faculty)

