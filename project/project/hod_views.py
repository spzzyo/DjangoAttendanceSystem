from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.models import Course,Session_Year, CustomUser, Student, Staff, Subject, Staff_Notifaction, Staff_Leave, Staff_Feedback, Student_Notifaction, Student_Leave

@login_required(login_url="/")
def HOME(request):
    student_count = Student.objects.all().count()
    staff_count = Staff.objects.all().count()
    course_count = Course.objects.all().count()
    subject_count = Subject.objects.all().count()

    context = {
    'student_count': student_count,
    'staff_count':staff_count,
    'course_count': course_count,
    'subject_count': subject_count,
}

    return render(request,'hod/home.html',context)


@login_required(login_url="/")
def add_student(request):
    course = Course.objects.all()
    session_year = Session_Year.objects.all()

    if request.method == "POST":
        profilePicture = request.FILES.get('profilePicture')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username= request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        session_year_id = request.POST.get('session_year_id')
        course_id = request.POST.get('course_id')

        if CustomUser.objects.filter(email= email).exists():
            messages.warning(request, 'Email exists already')
            return redirect('add_student')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username exists already')
            return redirect('add_student')
        
        else:
            user= CustomUser(

                first_name=first_name,
                last_name=last_name,
                username = username,
                password= password,
                email= email,
                profilePicture= profilePicture,
                user_type= 3
                
            )
            user.set_password(password)
            user.save()

            course = Course.objects.get(id = course_id)
            session_year = Session_Year.objects.get(id = session_year_id)


            student = Student(
                admin = user,
                address = address,
                session_year_id = session_year,
                course_id = course,
                gender = gender,
            )
            student.save()
            messages.success(request, 'Student data Saved')
            return redirect('add_student')



    context = {
        'course': course,
        'session_year': session_year,

    }

    return render(request, 'hod/add_student.html',context)

@login_required(login_url="/")
def view_student(request):
    student = Student.objects.all()
    context ={
        'student': student,

    }
    return render(request, 'hod/view_student.html',context)

@login_required(login_url="/")
def edit_student(request,id):
    student = Student.objects.filter(id = id)
    course = Course.objects.all()
    session_year = Session_Year.objects.all()
    context={
        'student': student,
        'course': course,
        'session_year': session_year,
    }

    return render(request, 'hod/edit_student.html', context)

@login_required(login_url="/")
def update_student(request):
    if request.method== "POST":
        student_id= request.POST.get('student_id')
        profilePicture = request.FILES.get('profilePicture')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username= request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        session_year_id = request.POST.get('session_year_id')
        course_id = request.POST.get('course_id')


        user = CustomUser.objects.get(id =student_id)
        user.first_name=first_name
        user.last_name=last_name
        user.username = username
        user.email= email
        if password!= None and password != "":
                user.set_password(password)

        if profilePicture != None:
            user.profilePicture = profilePicture
        
        user.save()

        student = Student.objects.get (admin = student_id)
        student.address = address
        student.gender = gender

        course = Course.objects.get(id= course_id)
        student.course_id = course

        session_year = Session_Year.objects.get(id= session_year_id)
        student.session_year_id= session_year

        student.save()
        messages.success(request, 'Records are successfully updated')
        return redirect(view_student)

    return render(request, 'hod/edit_student.html')

@login_required(login_url="/")
def delete_student(request, admin ):
    student = CustomUser.objects.get(id = admin)
    student.delete()
    messages.success(request, 'Successfully Deleted')
    return redirect(view_student)

@login_required(login_url="/")
def add_course(request):
    if request.method == "POST":
        course_name = request.POST.get('course_name')

        course = Course(
            name = course_name,
        )

        course.save()
        messages.success(request, 'Successfully ADDED')

        return redirect('add_course')
    return render(request, 'hod/add_course.html')

@login_required(login_url="/")
def view_course(request):
    course= Course.objects.all()
    context={
        'course' : course,
    }
    return render (request, 'hod/view_course.html',context)

@login_required(login_url="/")
def edit_course(request,id):
   
    course = Course.objects.get(id = id)

    context={
        'course': course,
    }

    return render(request, 'hod/edit_course.html', context)

@login_required(login_url="/")
def update_course(request):
    if request.method =="POST":
        name = request.POST.get('course_name')
        course_id = request.POST.get('course_id')

        course =Course.objects.get(id= course_id)
        course.name = name

        course.save()
        messages.success(request, 'Successfully ADDED')

        return redirect('view_course')
    
    return render(request, 'hod/edit_course.html')

@login_required(login_url="/")
def delete_course(request,id):
    course = Course.objects.get(id = id)
    course.delete()
    messages.success(request, 'Successfully Deleted')
    return redirect(view_course)

@login_required(login_url="/")
def add_staff(request):
    if request.method == "POST":
        profilePicture = request.FILES.get('profilePicture')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username= request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        address = request.POST.get('address')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'User with same email exists already')
            return redirect('add_staff')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'User with same username exists already')
            return redirect('add_staff')
        
        else :
            user=CustomUser(first_name=first_name, last_name=last_name, email= email, profilePicture=profilePicture, username=username, user_type=2)
            user.set_password(password)
            user.save()

            staff = Staff(
                admin = user,
                address = address,
                gender = gender,
            )

            staff.save()
            messages.success(request, 'Staff data Saved')
            return redirect ('add_staff')


    return render(request, 'hod/add_staff.html')

@login_required(login_url="/")
def view_staff(request):

    staff = Staff.objects.all()
    context ={
        'staff': staff,

    }
    return render(request, 'hod/view_staff.html',context)

@login_required(login_url="/")
def edit_staff(request,id):
    staff = Staff.objects.filter(id = id)
    context={
        'staff': staff,
    }

    return render(request, 'hod/edit_staff.html', context)

@login_required(login_url="/")
def update_staff(request):
    if request.method== "POST":
        staff_id= request.POST.get('staff_id')
        profilePicture = request.FILES.get('profilePicture')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username= request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        

        user = CustomUser.objects.get(id= staff_id)
        user.first_name=first_name
        user.last_name=last_name
        user.username = username
        user.email= email
        if password!= None and password != "":
                user.set_password(password)

        if profilePicture != None:
            user.profilePicture = profilePicture
        
        user.save()

        staff = Staff.objects.get (admin = staff_id)
        staff.address = address
        staff.gender = gender

    

        staff.save()
        messages.success(request, 'Records are successfully updated')
        return redirect(view_staff)
    
    return render(request, 'hod/edit_staff.html')

@login_required(login_url="/")
def delete_staff(request,id):
    staff = Staff.objects.get(id = id)
    staff.delete()
    messages.success(request, 'Successfully Deleted')
    return redirect(view_staff)

@login_required(login_url="/")
def add_subject(request):
    course = Course.objects.all()
    staff = Staff.objects.all()
    context ={
        'course': course,
        'staff': staff,
    }

    if request.method == "POST":
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')

        course = Course.objects.get(id = course_id)
        staff = Staff.objects.get(id = staff_id)

        subject = Subject(
            name = subject_name,
            course = course,
            staff = staff,
        )
        subject.save()
        messages.success(request, 'Successfully Added')
        return redirect('add_subject')
    
    return render(request, 'hod/add_subject.html', context)

@login_required(login_url="/")
def view_subject(request):

    subject = Subject.objects.all()

    context ={
        'subject' : subject,
    }

    return render(request, 'hod/view_subject.html', context)

@login_required(login_url="/")
def edit_subject(request,id):

    subject = Subject.objects.get(id = id)
    course = Course.objects.all()
    staff = Staff.objects.all()

    context={
        'subject': subject,
        'course': course,
        'staff': staff,
    }

    return render(request, 'hod/edit_subject.html', context)

@login_required(login_url="/")
def update_subject(request):
    if request.method =="POST":
        subject_id = request.POST.get('subject_id')
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id= request.POST.get('staff_id')

        course = Course.objects.get(id = course_id)
        staff = Staff.objects.get(id = staff_id)
        subject = Subject(
            name = subject_name,
            id = subject_id,
            course = course,
            staff = staff,

        )

    

        subject.save()
        messages.success(request, 'Successfully Updated')

        return redirect('view_subject')
    
    return render(request, 'hod/edit_subject.html')


@login_required(login_url="/")
def delete_subject(request,id):
    subject = Subject.objects.get(id = id)
    subject.delete()
    messages.success(request, 'Successfully Deleted')
    return redirect(view_subject)


@login_required(login_url="/")
def add_session(request):
    if request.method == 'POST':
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')

        session_year = Session_Year(
            session_start = session_year_start,
            session_end = session_year_end
        )

        session_year.save()

        messages.success(request, 'session created successfully')
        return redirect('add_session')

    return render(request, 'hod/add_session.html')


@login_required(login_url="/")
def view_session(request):

    session = Session_Year.objects.all()

    context = {
        'session': session
    }

    return render(request, 'hod/view_session.html', context)


@login_required(login_url="/")
def edit_session(request, id):
    session = Subject.objects.get(id = id)
    context = {
        'session' : session
    }

    return render(request, 'hod/edit_session.html', context)


@login_required(login_url="/")
def update_session(request):
    if request.method == "POST":
        session_id = request.POST.get('session_id')
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')

        session = Session_Year.objects.get(id=session_id)
        session.session_start = session_year_start
        session.session_end = session_year_end
        
        session.save()
        messages.success(request, 'Records Are Successfully Updated')
        return redirect('view_session')

    return render(request, 'hod/view_session.html')


@login_required(login_url="/")
def delete_session(request, id):

    session = Session_Year.objects.get(id = id)
    session.delete()
    messages.success(request, 'Session deleted successfully')
    return redirect('view_session')

@login_required(login_url="/")
def staff_send_notification(request):
    staff = Staff.objects.all()
    see_notification = Staff_Notifaction.objects.all()

    context={
        'staff': staff,
        'see_notification': see_notification,
    }

    return render(request, 'hod/staff_notification.html', context)

@login_required(login_url="/")
def staff_save_notification(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        message = request.POST.get('message')

        staff = Staff.objects.get(admin = staff_id)
        notification = Staff_Notifaction(
            staff_id=staff,
            message = message,
        )
        notification.save()
        messages.success(request, 'Notification Sent Successfully')

        return redirect('staff_send_notification')
    
    return render(request, 'hod/staff_notification.html')

@login_required(login_url="/")
def staff_leave_view(request):
    staff_leave= Staff_Leave.objects.all()

    context={
        'staff_leave':staff_leave,
    }

    return render(request, 'hod/staff_leave.html',context)

@login_required(login_url="/")
def staff_leave_approve(request,id):
    leave = Staff_Leave.objects.get(id = id)
    leave.status = 1
    leave.save()
    return redirect('staff_leave_view')

@login_required(login_url="/")
def staff_leave_disapprove(request,id):
    leave = Staff_Leave.objects.get(id = id)
    leave.status = 2
    leave.save()
    return redirect('staff_leave_view')


@login_required(login_url="/")
def staff_feedback_reply(request):
    feedback = Staff_Feedback.objects.all()

    context = {
        'feedback':feedback,
    }
    return render(request, 'hod/staff_feedback_reply.html', context)

@login_required(login_url="/")
def staff_feedback_reply_save(request):
    if request.method == "POST":
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback')
        print(feedback_id)

        hod_feedback = Staff_Feedback.objects.get(id = feedback_id)
        hod_feedback.reply = feedback_reply

        hod_feedback.save()
        messages.success(request, 'Reply Sent Successfully')
        return redirect('staff_feedback_reply')
    return render(request, 'hod/staff_feedback_reply.html')



@login_required(login_url="/")
def student_send_notification(request):
    student = Student.objects.all()
    see_notification = Student_Notifaction.objects.all()

    context={
        'student': student,
        'see_notification': see_notification,
    }

    return render(request, 'hod/student_notification.html', context)

@login_required(login_url="/")
def student_save_notification(request):

    if request.method == "POST":
        student_id = request.POST.get('student_id')
        message = request.POST.get('message')

        student = Student.objects.get(admin = student_id)
        notification = Student_Notifaction(
            student_id=student,
            message = message,
        )
        notification.save()
        messages.success(request, 'Notification Sent Successfully')

        return redirect('student_send_notification')
    
    return render(request, 'hod/student_notification.html')


@login_required(login_url="/")
def student_leave_view(request):
    student_leave= Student_Leave.objects.all()

    context={
        'student_leave':student_leave,
    }

    return render(request, 'hod/student_leave.html',context)

@login_required(login_url="/")
def student_leave_approve(request,id):
    leave = Student_Leave.objects.get(id = id)
    leave.status = 1
    leave.save()
    return redirect('student_leave_view')

@login_required(login_url="/")
def student_leave_disapprove(request,id):
    leave = Student_Leave.objects.get(id = id)
    leave.status = 2
    leave.save()
    return redirect('student_leave_view')