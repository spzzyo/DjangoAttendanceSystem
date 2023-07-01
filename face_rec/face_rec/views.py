from django.shortcuts import render,redirect,HttpResponse


def loginpage(request):
    return render(request, 'login.html')