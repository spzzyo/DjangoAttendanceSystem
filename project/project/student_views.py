from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import Student, Student_Notifaction, Student_Leave
from django.contrib import messages

def home(request):

    return render(request, 'student/home.html')

def student_notification(request):
    student = Student.objects.filter(admin = request.user.id)
    for i in student:
        student_id = i.id
        notification = Student_Notifaction.objects.filter(student_id = student_id)

        context ={
            'notification': notification,
        }

        return render(request, 'student/notifications.html',context)
    

def student_notification_mark_as_done(request,status):
    notification = Student_Notifaction.objects.get(id = status)
    notification.status = 1
    notification.save()

    return redirect('student_notification')


def student_leave(request):

    student = Student.objects.filter(admin = request.user.id)
    for i in student:
        student_id = i.id

        student_leave_history = Student_Leave.objects.filter(student_id = student_id)
        context = {
            'student_leave_history': student_leave_history,
        }

    return render(request,'student/student_leave.html',context)


def student_leave_save(request):
    if request.method == "POST":
        leave_date = request.POST.get('date')
        leave_message = request.POST.get('message')

        student = Student.objects.get(admin = request.user.id)

        leave = Student_Leave(
            student_id = student,
            date = leave_date,
            message = leave_message,
        )

        leave.save()
        messages.success(request, 'Successfully Submitted')

        return redirect ('student_leave')
    

    