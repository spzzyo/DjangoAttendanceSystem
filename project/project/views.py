from django.shortcuts import render,redirect,HttpResponse
from app.emailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import CustomUser

def base(request):
    return render(request,'base.html')

def loginpage(request):
    return render(request, 'login.html')

def doLogin(request):
    if request.method == 'POST':
        user= EmailBackEnd.authenticate(request,
                                        username=request.POST.get('email'),
                                        password=request.POST.get('password'),)
        if user!=None:
            login(request, user)
            user_type= user.user_type
            if user_type == '1':
                return redirect('hod_home')
            elif user_type == '2':
                return redirect('staff_home')
            elif user_type == '3':
                return redirect('student_home')
            else:
                messages.error(request, 'Email or Password is invalid')
                return redirect('loginpage')
        else:
            messages.error(request, 'Email or Password is invalid')
            return redirect('loginpage')
        
def doLogout(request):
    logout(request)
    return redirect(loginpage)

def PROFILE(request):
    user = CustomUser.objects.get(id=request.user.id)
    context = {
        'user': user,
    }
    return render(request,'profile.html',context)

def PROFILE_UPDATE(request):
    if request.method == 'POST':
        profilePicture = request.FILES.get('profilePicture')
        first_name =request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username= request.POST.get('username')
        password= request.POST.get('password')

        print(first_name)

        try:
            customuser = CustomUser.objects.get(id= request.user.id)

            customuser.first_name =first_name
            customuser.last_name= last_name

            
            if password!= None and password != "":
                customuser.set_password(password)

            if profilePicture != None:
                customuser.profilePicture = profilePicture
                
            customuser.save()
            messages.success(request,'uploaded!')
            redirect('profile')
        except:
            messages.error(request,'Failure')
            


    return render(request,'profile.html')