from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import Staff,Staff_Notifaction,Staff_Leave, Staff_Feedback
from django.contrib import messages


@login_required(login_url="/")
def home(request):
    # student_count = Student.objects.all().count()
    # staff_count = Staff.objects.all().count()
    # course_count = Course.objects.all().count()
    # subject_count = Subject.objects.all().count()

#     context = {
#     'student_count': student_count,
#     'staff_count':staff_count,
#     'course_count': course_count,
#     'subject_count': subject_count,
# }

    return render(request,'staff/home.html')

def staff_notification(request):
    staff = Staff.objects.filter(admin = request.user.id)
    for i in staff:
        staff_id = i.id
        notification = Staff_Notifaction.objects.filter(staff_id = staff_id)

        context ={
            'notification': notification,
        }

        return render(request, 'staff/notifications.html',context)
    

def staff_notification_mark_as_done(request,status):
    notification = Staff_Notifaction.objects.get(id = status)
    notification.status = 1
    notification.save()

    return redirect('staff_notification')

def staff_leave(request):

    staff = Staff.objects.filter(admin = request.user.id)
    for i in staff:
        staff_id = i.id

        staff_leave_history = Staff_Leave.objects.filter(staff_id = staff_id)
        context = {
            'staff_leave_history': staff_leave_history,
        }

    return render(request,'staff/staff_leave.html',context)


def staff_leave_save(request):
    if request.method == "POST":
        leave_date = request.POST.get('date')
        leave_message = request.POST.get('message')

        staff = Staff.objects.get(admin = request.user.id)

        leave = Staff_Leave(
            staff_id = staff,
            date = leave_date,
            message = leave_message,
        )

        leave.save()
        messages.success(request, 'Successfully Submitted')

        return redirect ('staff_leave')
    

def staff_feedback(request):
    staff_id = Staff.objects.get(admin=request.user.id)
    
    staff_feedback_history = Staff_Feedback.objects.filter(staff_id = staff_id)

    context = {
        'staff_feedback_history':staff_feedback_history,
    }

    return render(request, 'staff/staff_feedback.html',context)

def staff_feedback_save(request):
    if request.method == "POST":
        message = request.POST.get('message')

        staff = Staff.objects.get(admin=request.user.id)
        
        feedback = Staff_Feedback(
            staff_id = staff,
            feedback = message,
            reply=""
        )

        feedback.save()
        messages.success(request, 'Feedback Sent Successfully')
        return redirect('staff_feedback_save')
    return render(request, 'staff/staff_feedback.html')



