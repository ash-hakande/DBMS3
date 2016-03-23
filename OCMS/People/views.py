from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from forms import *
from Courses.models import *
from Mail.models import *
from CourseMatter.models import *
from django.core.exceptions import ObjectDoesNotExist

def isFaculty(user):
	if user.username[0]=='F':
		return True
	return False

def isStudent(user):
	if user.username[0]=='S':
		return True
	return False

def isParent(user):
	if user.username[0]=='P':
		return True
	return False

def isAdmin(user):
	if user.username[0]=='A':
		return True
	return False

def authenticateUser(username,password,usertype,request):
	initials = {Student : 'S', Faculty : 'F', Parent : 'P', Admin : 'A'}
	if usertype in initials.keys():
		user = authenticate(username = initials[usertype]+username, password = password)
		if user is not None and user.username[0]=='S':
			student = Student.objects.get(username = user.username[1:])
			if student is not None:
				login(request, user)
				return student
			return None
		elif user is not None and user.username[0]=='F':
			faculty = Faculty.objects.get(username = user.username[1:])
			if faculty is not None:
				login(request, user)
				return faculty
			return None
		elif user is not None and user.username[0]=='P':
			parent = Parent.objects.get(username = user.username[1:])
			if parent is not None:
				login(request, user)
				return parent
			return None
		elif user is not None and user.username[0]=='A':
			adminuser = Admin.objects.get(username = user.username[1:])
			if adminuser is not None:
				login(request, user)
				return adminuser
			return None
		else : return None
	return None

def getFaculty(user):
	try:
		faculty = Faculty.objects.get(username = user.username[1:])
	except ObjectDoesNotExist:
		return None
	return faculty

def getStudent(user):
	try:
		student = Student.objects.get(username = user.username[1:])
	except ObjectDoesNotExist:
		return None
	return student 

def getParent(user):
	try:
		parent = Parent.objects.get(username = user.username[1:])
	except ObjectDoesNotExist:
		return None
	return parent 

# Create your views here.

def homepage(request):
	return render(request, "People/login_href.html")

def studentSignUp(request):
    if request.method=='POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            cleanedData = form.cleaned_data
            user = User.objects.create_user('S'+cleanedData.get('username'),password=cleanedData.get('password'))
            user.first_name = cleanedData.get('firstName')
            user.last_name = cleanedData.get('lastName')
            user.save()
            student = Student.objects.create()
            student.firstName = cleanedData.get('firstName')
            student.lastName = cleanedData.get('lastName')
            student.username = cleanedData.get('username')
            student.password = cleanedData.get('password')
            student.save()
            print 'Saved'
            return HttpResponseRedirect('/homepage')
        else:
            return HttpResponse("Email Id or Phone no. has been already Registered (Validation Failed)")
        
    else:
        form = StudentSignUpForm()
        context = {
        "who" : "Student",
        "title":"Register On Coursera",
        "form": form,
        }
        return render(request,"Signup/signup_student.html",context)

def facultySignUp(request):
    if request.method=='POST':
        form = FacultySignUpForm(request.POST)
        if form.is_valid():
            cleanedData = form.cleaned_data
            user = User.objects.create_user('F'+cleanedData.get('username'),password=cleanedData.get('password'))
            user.first_name = cleanedData.get('firstName')
            user.last_name = cleanedData.get('lastName')
            user.save()
            faculty = Faculty.objects.create()
            faculty.firstName = cleanedData.get('firstName')
            faculty.lastName = cleanedData.get('lastName')
            faculty.username = cleanedData.get('username')
            faculty.password = cleanedData.get('password')
            faculty.save()
            print 'Saved'
            return HttpResponseRedirect('/homepage')
        else:
            return HttpResponse("Email Id or Phone no. has been already Registered (Validation Failed)")
    else:
        form = FacultySignUpForm()
        context = {
        "who" : "Faculty",
        "title":"Register On Coursera",
        "form": form,
        }
        return render(request,"Signup/signup_faculty.html",context)

def parentSignUp(request):
    if request.method=='POST':
        form = ParentSignUpForm(request.POST)
        print form.is_valid()
        if form.is_valid():
            cleanedData = form.cleaned_data
            user = User.objects.create_user('P'+cleanedData.get('username'),password=cleanedData.get('password'))
            user.first_name = cleanedData.get('firstName')
            user.last_name = cleanedData.get('lastName')
            user.save()
            parent = Parent.objects.create()
            parent.firstName = cleanedData.get('firstName')
            parent.lastName = cleanedData.get('lastName')
            parent.username = cleanedData.get('username')
            parent.password = cleanedData.get('password')
            raw = cleanedData.get('child')
            Students = Student.objects.all()
            for s in Students:
            	if str(s) == raw:
            		child = s
            		break
            parent.child = child
            parent.save()
            print 'Saved'
            return HttpResponseRedirect('/homepage')
        else:
            return HttpResponse("Email Id or Phone no. has been already Registered (Validation Failed)")
        
    else:
        form = ParentSignUpForm()
        context = {
        "who" : "Parent",
        "title":"Register On Coursera",
        "form": form,
        }
        return render(request,"Signup/signup_parent.html",context)



def studentLogin(request):
	if request.method=='POST':
		form = StudentLoginForm(request.POST)
		if form.is_valid():
			cleanedData = form.cleaned_data
			student = authenticateUser(cleanedData.get('username'), cleanedData.get('password'), Student, request)
			if student is not None:
				context = {
					'my_courses_length' : 2,
					'my_courses' : ['Operating System','Course'],
				}
				print student
				return HttpResponseRedirect('/student/home/')
	else:
		form = StudentLoginForm()
		context = {
			"usertype" : "Student",
			"form" : form,
		}
		return render(request, 'Signup/login.html', context)

def facultyLogin(request):
	if request.method=='POST':
		form = FacultyLoginForm(request.POST)
		if form.is_valid():
			cleanedData = form.cleaned_data
			faculty = authenticateUser(cleanedData.get('username'), cleanedData.get('password'), Faculty, request)
			if faculty is not None:
				context = {
					'my_courses_length' : 2,
					'my_courses' : ['Operating System','Course'],
				}
				return render(request,"student_update/my_courses_bs.html",context)
	else:
		form = FacultyLoginForm()
		context = {
			"usertype" : "Student",
			"form" : form,
		}
		return render(request, 'Signup/login.html', context)

def parentLogin(request):
	if request.method=='POST':
		form = ParentLoginForm(request.POST)
		if form.is_valid():
			cleanedData = form.cleaned_data
			parent = authenticateUser(cleanedData.get('username'), cleanedData.get('password'), Parent, request)
			if parent is not None:
				context = {
					'my_courses_length' : 2,
					'my_courses' : ['Operating System','Course'],
				}
				print parent
				return HttpResponseRedirect('/parent/home/')
	else:
		form = StudentLoginForm()
		context = {
			"usertype" : "Parent",
			"form" : form,
		}
		return render(request, 'Signup/login.html', context)



#@user_passes_test(isStudent, login_url = '/student/login/')
def studentHomePage(request):
	student = getStudent(request.user)
	my_courses = []
	try:
		registered = Registered.objects.filter(studentID = student)
		for reg in registered:
			my_courses.append(reg.courseID)
	except:
		pass
	context = {
		'my_courses_length' : len(my_courses),
		'my_courses' : my_courses,
	}
	return render(request,"student_update/my_courses_bs.html",context)

#@user_passes_test(isStudent, login_url = '/student/login/')
def studentMyCourseDisplay(request):
	url = request.path
	if url[-1]=='/':url=url[:-1]
	courseid = int(url[url.rfind('/')+1:])
	course = Course.objects.get(courseID = courseid)
	coursecontent = CourseContent.objects.get(courseID = course)
	if request.method=='POST':
		pass
	else:
		context = {
			'course' : course,
			'coursecontent' : coursecontent,
		}
		return render(request, 'student_update/course_current_bs.html', context)

#@user_passes_test(isStudent, login_url = '/student/login/')
def studentAllCourseList(request):
	all_courses = []
	try:
		all_courses = Course.objects.all()
	except:
		print 'Error in retrieving all courses'
		pass
	links = []
	for course in all_courses:
		links.append('/student/courselist/%d/'%(course.courseID))
	context = {
		'all_courses' : all_courses,
		'links' : links,
	}
	return render(request,"student_update/courselist_student_bs.html",context)

#@user_passes_test(isStudent, login_url = '/student/login/')
def studentCourseDetails(request):
	url = request.path
	if url[-1]=='/':url=url[:-1]
	courseid = int(url[url.rfind('/')+1:])
	try:
		course = Course.objects.get(courseID = courseid)
	except:
		pass
	if request.method=='POST':
		student = getStudent(request.user)
		if student is not None:
			reg = Registered.objects.create(courseID = course, studentID = student)
			reg.save()
			return HttpResponse("Successfully registered!")
		else:
			return HttpResponse("No student logged in!")
	else:
		context = {
			'course' : course,
		}
		print course
		return render(request,"student_update/course_details_bs.html",context)


#@user_passes_test(isStudent, login_url = '/student/login/')
def studentMailCompose(request):
	if request.method=='POST':
		form = StudentMailComposeForm(request.POST)
		print form.is_valid()
		if form.is_valid():
			cleanedData = form.cleaned_data
			student = getStudent(request.user)
			faculties = Faculty.objects.all()
			faculty = None
			for f in faculties:
				if str(f)==cleanedData.get('facultyName'):
					faculty = f
					break
			if student is not None and faculty is not None:
				mail = StudentToFacultyMail.objects.create(studentID = student, facultyID = faculty)
				mail.mailSubject = cleanedData.get('mailSubject')
				mail.mailText = cleanedData.get('mailText')
				mail.save()
				return HttpResponse("Mail sent Successfully!")
			else:
				return HttpResponse("Invalid Faculty!")
		else:
			return HttpResponse("Invalid fields!")
	else:
		form = StudentMailComposeForm()
		context = {
			# "usertype" : "Faculty",
			"form" : form,
		}
		return render(request, 'student_update/compose_bs.html', context)

#@user_passes_test(isStudent, login_url = '/student/login/')
def studentMailSent(request):
	student = getStudent(request.user)
	sent_mails = StudentToFacultyMail.objects.filter(studentID = student)
	context = {
		'sent_mails' : sent_mails,
	}
	return render(request, 'student_update/sent_bs.html', context)

def studentMailInbox(request):
	student = getStudent(request.user)
	inbox_mails = FacultyToStudentMail.objects.filter(studentID = student)
	context = {
		'inbox_mails' : inbox_mails,
	}
	return render(request, 'student_update/inbox_bs.html', context)

#@user_passes_test(isStudent, login_url = '/student/login/')
def studentMailHome(request):
	context = {

	}
	return render(request, 'student_update/mail_bs.html', context)

#@user_passes_test(isStudent, login_url = '/student/login/')
def studentMailRecievedBody(request):
	url = request.path
	if url[-1]=='/':url=url[:-1]
	mailid = int(url[url.rfind('/')+1:])
	mail = FacultyToStudentMail.objects.get(mailID = mailid)
	context = {
		"mail" : mail,
	}
	return render(request, 'student_update/recieved_body_bs.html', context)

#@user_passes_test(isStudent, login_url = '/student/login/')
def studentMailSentBody(request):
	url = request.path
	if url[-1]=='/':url=url[:-1]
	mailid = int(url[url.rfind('/')+1:])
	mail = StudentToFacultyMail.objects.get(mailID = mailid)
	context = {
		"mail" : mail,
	}
	return render(request, 'student_update/sent_body_bs.html', context)

#@user_passes_test(isStudent, login_url = '/student/login/')
def studentTest(request):
	url = request.path
	if url[-1] == '/':
		url = url[:-1]
	testid = int(url[url.rfind('/')+1:])
	url = url[:url.rfind('/')-1]
	url = url[:-6]
	courseID = int(url[url.rfind('/')+1:])
	test = None
	questions = []
	try:
		test = Test.objects.get(testID = testid)
	except:
		pass
	testDetails = test.questions.all()
	for detail in testDetails:
		string = detail.questionText
		string = string + detail.choice1 + detail.choice2 + detail.choice3 + detail.choice4
		questions.append(string)
	context = {
		"questions" : questions
	}
	if request.method == 'POST':
		form = TestTake(request.POST)
		if form.is_valid():
			cleanedData = form.cleaned_data
			option = []
			option[1] = cleanedData('choice1')
			option[2] = cleanedData('choice2')
			option[3] = cleanedData('choice3')
			option[4] = cleanedData('choice4')
			option[5] = cleanedData('choice5')
			option[6] = cleanedData('choice6')
			option[7] = cleanedData('choice7')
			option[8] = cleanedData('choice8')
			option[9] = cleanedData('choice9')
			option[10] = cleanedData('choice10')
			marks = 0
			i = 1
			for question in testDetails:
				if option[i] == question.correct:
					marks = marks + 1
			
			evaluation = Evaluation.objects.create()
			evaulation.studentID = getStudent(request.user)
			evaulation.testID = testID
			evaulation.marks = marks
			evaulation.save()
			print 'TestMarks Saved', "\n"
			return HttpResponseRedirect('/student/home/')
		else:
			pass
	return render(request, "People/take_test.html", context)

####################### PARENT FEATURES ##########################

#@user_passes_test(isParent, login_url = '/parent/login/')
def parentHomePage(request):
	parent = getParent(request.user)
	child_courses_names = []
	try:
		child_courses = Registered.objects.filter(studentID = parent.child)
		for course in child_courses:
			child_courses_names.append(course.courseName)
	except:
		pass
	context = {
		'child_courses_length' : len(child_courses_names),
		'child_courses' : child_courses_names,
	}	
	return render(request,"People/first_page_bs.html",context)

#@user_passes_test(isParent, login_url = '/parent/login/')
def parentMailCompose(request):
	if request.method=='POST':
		form = StudentMailComposeForm(request.POST)
		print form.is_valid()
		if form.is_valid():
			cleanedData = form.cleaned_data
			parent = getParent(request.user)
			faculties = Faculty.objects.all()
			faculty = None
			for f in faculties:
				if str(f)==cleanedData.get('facultyName'):
					faculty = f
					break
			if parent is not None and faculty is not None:
				mail = ParentToFacultyMail.objects.create(parentID = parent, facultyID = faculty)
				mail.mailSubject = cleanedData.get('mailSubject')
				mail.mailText = cleanedData.get('mailText')
				mail.save()
				return HttpResponse("Mail sent Successfully!")
			else:
				return HttpResponse("Invalid Faculty!")
		else:
			return HttpResponse("Invalid fields!")
	else:
		form = ParentMailComposeForm()
		context = {
			# "usertype" : "Faculty",
			"form" : form,
		}
		return render(request, 'Signup/compose_bs.html', context)

#@user_passes_test(isParent, login_url = '/parent/login/')
def parentMailSent(request):
	parent = getParent(request.user)
	sent_mails = ParentToFacultyMail.objects.filter(parentID = parent.parentID)
	context = {
		'mails' : sent_mails,
	}
	return render(request, 'Signup/sent_bs.html', context)

#@user_passes_test(isParent, login_url = '/parent/login/')
def parentMailInbox(request):
	parent = getParent(request.user)
	inbox_mails = FacultyToParentMail.objects.filter(parentID = parent.parentID)
	context = {
		'mails' : inbox_mails,
	}
	return render(request, 'Signup/inbox_bs.html', context)

def parentMailHome(request):
	context = {

	}
	return render(request, 'Signup/mail_bs.html', context)

#@user_passes_test(isParent, login_url = '/parent/login/')
def parentMailRecievedBody(request):
	url = request.path
	if url[-1]=='/':url=url[:-1]
	mailid = int(url[url.rfind('/')+1:])
	mail = FacultyToParentMail.objects.get(mailID = mailid)
	context = {
		"mail" : mail,
	}
	return render(request, 'Signup/recieved_body_bs.html', context)

#@user_passes_test(isParent, login_url = '/parent/login/')
def parentMailSentBody(request):
	url = request.path
	if url[-1]=='/':url=url[:-1]
	mailid = int(url[url.rfind('/')+1:])
	mail = ParentToFacultyMail.objects.get(mailID = mailid)
	context = {
		"mail" : mail,
	}
	return render(request, 'Signup/sent_body_bs.html', context)


#@user_passes_test(isFaculty, login_url = '/faculty/login/')
def facultyHomePage(request):
	faculty = getFaculty(request.user)
	print request.user
	my_courses = []
	try:
		all_courses = Course.objects.all()
		for course in all_courses:
			if faculty in course.faculties.all():
				my_courses.append(course)
	except:
		print 'Error'
		pass
	print my_courses
	context = {
		'my_courses_length' : len(my_courses),
		'my_courses' : my_courses,
		'faculty' : faculty,
	}
	return render(request,"People/my_courses_bs.html",context)

#@user_passes_test(isFaculty, login_url = '/faculty/login/')
def facultyCourseDetails(request):
	url = request.path
	if url[-1]=='/':url=url[:-1]
	courseid = int(url[url.rfind('/')+1:])
	try:
		course = Course.objects.get(courseID = courseid)
	except:
		pass
	context = {
		'course' : course,
	}

#@user_passes_test(isFaculty, login_url = '/faculty/login/')
def facultyAddCourse(request):
	if request.method=='POST':
		form=FacultyAddCourseForm()
		if form.is_valid():
			cleanedData = form.cleaned_data
			faculty = getFaculty(request.user)
			# course = 
	else:
		form = FacultyAddCourseForm()
		context = {
			"form" : form,
		}
		render(request,"People/add_courses_bs.html",context)


#@user_passes_test(isFaculty, login_url = '/faculty/login/')
def facultyMailCompose(request):
	if request.method=='POST':
		form = FacultyMailComposeForm(request.POST)
		print form.is_valid()
		if form.is_valid():
			cleanedData = form.cleaned_data
			faculty = getFaculty(request.user)
			parents = Parent.objects.all()
			parent = None
			for p in parents:
				if str(p)==cleanedData.get('facultyName'):
					parent = p
					break
			if faculty is not None and parent is not None :
				mail = FacultyToParentMail.objects.create(facultyID = faculty, parentID = parent)
				mail.mailSubject = cleanedData.get('mailSubject')
				mail.mailText = cleanedData.get('mailText')
				mail.save()
				return HttpResponse("Mail sent Successfully!")
			students = Student.objects.all()
			student = None
			for s in students:
				if str(s)==cleanedData.get('facultyName'):
					student=s
					break
			if student is not None and faculty is not None:
				mail = FacultyToStudentMail.objects.create(studentID = student, facultyID = faculty)
				mail.mailSubject = cleanedData.get('mailSubject')
				mail.mailText = cleanedData.get('mailText')
				mail.save()
				return HttpResponse("Mail sent Successfully!")
			else:
				return HttpResponse("Invalid Faculty!")
		else:
			return HttpResponse("Invalid fields!")
	else:
		form = FacultyMailComposeForm()
		context = {
			# "usertype" : "Faculty",
			"form" : form,
		}
		return render(request, 'People/compose_bs.html', context)

#@user_passes_test(isFaculty, login_url = '/faculty/login/')
def facultyMailSent(request):
	faculty = getFaculty(request.user)
	sent_mails_parent = FacultyToParentMail.objects.filter(facultyID = faculty)
	sent_mails_student = FacultyToStudentMail.objects.filter(facultyID = faculty)
	context = {
		'sent_mails_parent' : sent_mails_parent,
		'sent_mails_student' : sent_mails_student,
	}
	return render(request, 'People/sent_bs.html', context)

#@user_passes_test(isFaculty, login_url = '/faculty/login/')
def facultyMailInbox(request):
	faculty = getFaculty(request.user)
	inbox_mails_parent = ParentToFacultyMail.objects.filter(facultyID = faculty)
	inbox_mails_student = StudentToFacultyMail.objects.filter(facultyID = faculty)
	context = {
		'inbox_mails_parent' : inbox_mails_parent,
		'inbox_mails_student' : inbox_mails_student,
	}
	return render(request, 'People/inbox_bs.html', context)

#@user_passes_test(isFaculty, login_url = '/faculty/login/')
def facultyMailHome(request):
	context = {

	}
	return render(request, 'student_update/mail_bs.html', context)

#@user_passes_test(isFaculty, login_url = '/faculty/login/')
def facultyMailRecievedBody(request):
	url = request.path
	if url[-1]=='/':url=url[:-1]
	mailid = int(url[url.rfind('/')+1:])
	url = url[:url.rfind('/')]
	fromtype = url[url.rfind('/')+1:]
	if fromtype=='parent':
		mail = ParentToFacultyMail.objects.get(mailID = mailid)
		context = {
			"from" : mail.parentID,
			"mail" : mail,
		}
		return render(request, 'People/recieved_body_bs.html', context)
	elif fromtype=='student':
		mail = ParentToFacultyMail.objects.get(mailID = mailid)
		context = {
			"from" : mail.studentID,
			"mail" : mail,
		}
		return render(request, 'People/recieved_body_bs.html', context)

#@user_passes_test(isFaculty, login_url = '/faculty/login/')
def facultyMailSentBody(request):
	url = request.path
	if url[-1]=='/':url=url[:-1]
	mailid = int(url[url.rfind('/')+1:])
	url = request.path
	if url[-1]=='/':url=url[:-1]
	mailid = int(url[url.rfind('/')+1:])
	url = url[:url.rfind('/')]
	fromtype = url[url.rfind('/')+1:]
	if fromtype=='parent':
		mail = FacultyToParentMail.objects.get(mailID = mailid)
		context = {
			"to" : mail.parentID,
			"mail" : mail,
		}
		return render(request, 'People/sent_body_bs.html', context)
	elif fromtype=='student':
		mail = StudentToFacultyMail.objects.get(mailID = mailid)
		context = {
			"to" : mail.studentID,
			"mail" : mail,
		}
		return render(request, 'People/sent_body_bs.html', context)

#@user_passes_test(isFaculty, login_url = '/faculty/login/')	
def facultyCourseContent(request):
	url = request.path
	if url[-1]=='/':url=url[:-1]
	courseid = int(url[url.rfind('/')+1:]) 
	faculty = getFaculty(request.user)
	course = Course.objects.get(courseID = courseid)
	courseContent = CourseContent.objects.filter(courseID = courseid)
	context = {
		'courseContent' : courseContent,
		'course' : course
	}
	return render(request,"People/courseinfo_faculty.html",context)


#@user_passes_test(isFaculty, login_url = '/faculty/login/')
def facultyAddTest(request):
	url = request.path
	if url[-1]=='/':url=url[:-1]
	url = url[:url.rfind('/')]
	courseid = int(url[url.rfind('/')+1:])
	if request.method=='POST':
		form = FacultyAddTestForm(request.POST)
		if form.is_valid():
			cleanedData = form.cleaned_data
			question1 = Question.objects.create()
			question1.questionText = cleanedData.get('Question1')
			question1.choice1 = cleanedData.get('Question1Option1')
			question1.choice2 = cleanedData.get('Question1Option2')
			question1.choice3 = cleanedData.get('Question1Option3')
			question1.choice4 = cleanedData.get('Question1Option4')
			question1.correct = cleanedData.get('Question1Answer')
			question1.save()

			question2 = Question.objects.create()
			question2.questionText = cleanedData.get('Question2')
			question2.choice1 = cleanedData.get('Question2Option1')
			question2.choice2 = cleanedData.get('Question2Option2')
			question2.choice3 = cleanedData.get('Question2Option3')
			question2.choice4 = cleanedData.get('Question2Option4')
			question2.correct = cleanedData.get('Question2Answer')
			question2.save()

			question3 = Question.objects.create()
			question3.questionText = cleanedData.get('Question3')
			question3.choice1 = cleanedData.get('Question3Option1')
			question3.choice2 = cleanedData.get('Question3Option2')
			question3.choice3 = cleanedData.get('Question3Option3')
			question3.choice4 = cleanedData.get('Question3Option4')
			question3.correct = cleanedData.get('Question3Answer')
			question3.save()

			question4 = Question.objects.create()
			question4.questionText = cleanedData.get('Question4')
			question4.choice1 = cleanedData.get('Question4Option1')
			question4.choice2 = cleanedData.get('Question4Option2')
			question4.choice3 = cleanedData.get('Question4Option3')
			question4.choice4 = cleanedData.get('Question4Option4')
			question4.correct = cleanedData.get('Question4Answer')
			question4.save()

			question5 = Question.objects.create()
			question5.questionText = cleanedData.get('Question5')
			question5.choice1 = cleanedData.get('Question5Option1')
			question5.choice2 = cleanedData.get('Question5Option2')
			question5.choice3 = cleanedData.get('Question5Option3')
			question5.choice4 = cleanedData.get('Question5Option4')
			question5.correct = cleanedData.get('Question5Answer')
			question5.save()

			test = Test.objects.create()
			test.questions.add(question1)
			test.questions.add(question2)
			test.questions.add(question3)
			test.questions.add(question4)
			test.questions.add(question5)
			test.save()

			course = Course.objects.get(courseID = courseid)
			cc = CourseContent.objects.get(courseID = course)
			cc.tests.add(test)
			cc.save()

			return HttpResponse("You have successfully added the assignment!\n")

		else:
			return HttpResponse("Assignment addition failed!")
	else:
		context = {

		}
		return render(request,"People/add_assignment.html", context)
	context= {

	}
	return render(request, "People/add_assignment.html/", context)

#@user_passes_test(isFaculty, login_url = '/faculty/login/')
def facultyAddAssignment(request):
	url = request.path
	if url[-1]=='/':url=url[:-1]
	url = url[:url.rfind('/')]
	courseid = int(url[url.rfind('/')+1:])
	if request.method=='POST':
		cleanedData = form.cleaned_data
		assignment = Assignment.objects.create(assignmentTitle=cleanedData.get('assignmentTitle'),assignmentText=cleanedData.get('assignmentText'))
		assignment.save()

		course = Course.objects.get(courseID = courseid)
		cc = CourseContent.objects.get(courseID = course)
		cc.assignments.add(assignment)
		return HttpResponse("Assignment added successfully!")
	else:
		context = {

		}
		return render(request, 'People/assignment_bs.html', context)

#@user_passes_test(isFaculty, login_url = '/faculty/login/')
def facultyAddLecture(request):
	url = request.path
	if url[-1]=='/':url=url[:-1]
	url = url[:url.rfind('/')]
	courseid = int(url[url.rfind('/')+1:])
	if request.method=='POST':
		cleanedData = form.cleaned_data
		lecture = Assignment.objects.create(lectureTitle=cleanedData.get('lectureTitle'),lectureText=cleanedData.get('lectureText'))
		lecture.lectureWeek=cleanedData.get('lectureWeek')
		lecture.save()

		course = Course.objects.get(courseID = courseid)
		cc = CourseContent.objects.get(courseID = course)
		cc.lectures.add(lecture)
		return HttpResponse("Assignment added successfully!")
	else:
		context = {

		}
		return render(request, 'People/lecture_bs.html', context)

def facultyViewAssignment(request):
	url = request.path
	if url[-1]=='/':url=url[:-1]
	assignmentid = int(url[url.rfind('/')+1:])
	assignment = Assignment.objects.get(assignmentID = assignmentid)
	context = {
		'assignment' : assignment
	}
	return render(request, 'People/faculty_show_assignment.html',context)

def facultyViewLecture(request):
	url = request.path
	if url[-1]=='/':url=url[:-1]
	lectureid = int(url[url.rfind('/')+1:])
	lecture = Lecture.objects.get(lectureID = lectureid)
	context = {
		'lecture' : lecture
	}
	return render(request, 'People/faculty_show_lecture.html',context)

def facultyViewTest(request):
	url = request.path
	if url[-1]=='/':url=url[:-1]
	testid = int(url[url.rfind('/')+1:])
	test = Test.objects.get(testID = testid)
	context = {
		'test' : test
	}
	return render(request, 'People/faculty_show_test.html',context)
	