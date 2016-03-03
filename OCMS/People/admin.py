from django.contrib import admin
from models import Student, Faculty, Parent, Admin

# Register your models here.

class StudentSite(admin.AdminSite):
	site_header = 'Welcome Student!'

class FacultySite(admin.AdminSite):
	site_header = 'Welcome Faculty!'

studentSite = StudentSite(name = 'student site')
facultySite = FacultySite(name = 'faculty site')

admin.site.register(Faculty)

