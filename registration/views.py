from django.shortcuts import render,redirect
from django.http import HttpResponse
from registration.models import Student
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def home(request):
      return render(request,"home.html")

    


def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
       
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("username or password is incorrect")

    return render(request,"login.html")




def registration_page(request):

    if request.method == "POST":

        username=request.POST.get('username')
        email=request.POST.get('email')  
        password=request.POST.get('password')
        confirmPassword=request.POST.get('confirmPassword')
        if password != confirmPassword:
            return HttpResponse ("wrong confirm password") 
        else:

            user=User.objects.create_user(username,email,password)
            user.save()
            return redirect('/login/')
       # if user.exists():
       #     messages.info(request,'Username already taken')
        #    return redirect('/register/')



    return render(request,"register.html")   

def data(request):
    all_members=Student.objects.all
    return render(request,"data.html",{'all':all_members})


def school(request):
    return render(request,"school.html")

def staff(request):
    return render(request,"staff.html")






