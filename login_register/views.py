from django.shortcuts import render
from .models import details
from django.contrib import messages
# Create your views here.
def basic(request):
    return render(request,'login_register/basic.html')

def register(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        if fname=='' or lname=='' or email=='' or pass1==''or pass2=='':
            messages.success(request,'No empty spaces are allowed')
            return render(request, 'login_register/register.html')
        else:
            if pass1==pass2 :
                c=details(fname=fname,lname=lname,email=email,password=pass1)
                c.save()
                return render(request,'login_register/thanks.html')
            else:
                messages.success(request, 'Passwords wont match')
                return render(request, 'login_register/register.html')
    else:
        return render(request,'login_register/register.html')

def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        all_data=details.objects.all()
        for i in all_data:
            if i.email == email:
                if i.password == password:
                    return render(request,'login_register/thanks.html')
                else:
                    messages.success(request,'Username or password won\'t match')
                    return render(request,'login_register/login.html')
    else:
        return render(request,'login_register/login.html')