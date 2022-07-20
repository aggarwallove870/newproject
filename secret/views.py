from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import auth
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from requests import session
from secret.models  import Courses
from django.contrib.auth.hashers import make_password
from django.contrib import messages
# Create your views here.
@login_required
def Dashboard(request):
    user_count= User.objects.filter(is_active=1).count()
    course_count=Courses.objects.filter(is_active=1).count()
    return render(request, 'secret/index.html',{"user":request.user,'user_count':user_count,'course_count':course_count})

def Login(request):
    msg = ""
    if(request.method=="POST"):
        username=request.POST.get('username')
        print(username)
        password=request.POST.get('password')
        print(password)
        user = auth.authenticate(username=username, password=password)
        print(user,"----USR------")
        if user:
            if user.is_superuser:
                auth.login(request, user)
                return redirect("/secret/")
            else:
                msg = "Login from Mobile App!"
        else:
            msg = "Incorrect Password!"
    print(msg)
    return render(request, 'secret/login.html',{"msg":msg});

def Register(request):
    return render(request, 'secret/register.html');

def ForgotPassword(request):
    return render(request, 'secret/forgot-password.html');

@login_required
def Settings(request):
    return render(request, 'secret/settings.html',{"msg":request.GET.get('q'),"err":request.GET.get('e')});


@login_required
def Profile(request):
    user_id = request.user.id
    print(user_id)
    msg = ""
    if request.method=="POST":
        u = request.user
        email=request.POST.get('email')
        fname=request.POST.get('first_name')
        lname=request.POST.get('last_name')
        email=email.strip()
        fname=fname.strip()
        lname=lname.strip()
        try:
           flag=None
           match=User.objects.filter(email=email).values_list('id')
           print(match)
           for i in match:
                print(i[0])
                if int(i[0])!=int(user_id):
                    flag =1
                    break
        except Exception as e:
           print(e)
        if(flag):
            err= "Mail already exists"
            return redirect("/secret/settings/?q="+msg+"&e="+err)
  
        if len(fname)<3 or len(lname)<3:
            err= "Length of first name and last name must be of minimum 3 characters"
            if fname=="" or lname =="" or email =="":
                err= "All mandatory fields must be filled"
            return redirect("/secret/settings/?q="+msg+"&e="+err)

        u.first_name = request.POST.get('first_name')
        u.last_name  = request.POST.get('last_name')
        u.email      = request.POST.get('email')
        u.save()
        msg="Information Updated!"
    return redirect("/secret/settings/?q="+msg)
@login_required
def ChangePassword(request):
    
    msg = ""
    err = ""
    if request.method=="POST":
        u  = request.user
        print(u,"REQUEST.USER")
        opwd  = request.POST.get('opwd')
        npwd  = request.POST.get('npwd')
        cnpwd = request.POST.get('cnpwd')
        opwd=opwd.strip()
        npwd =npwd.strip()
        cnpwd=cnpwd.strip()
        print(u, "uuu")
        print(opwd,"opwd")
        print(npwd, "npwd")
        print(cnpwd, "cnpwd")
       
        if u.check_password(opwd) == True:
            print(u.check_password(opwd))
            print('true,' )
            
            if len(npwd)>3 or len(cnpwd)>3:
                print('graeater')
                if npwd == cnpwd:
                    print('equal')
                    u.set_password(npwd)
                    u.save()
                    msg="Password Updated!"
                    print("HERE BUDYDY")
                    request.session['is_chnaged'] = "Changed sucessully"
                    return redirect('Dashboard')
                    # messages.success(request, 'Form submission successful')
                else:
                    print("not match")
                    err="New passwords didn't match!"
            else:
                print("leng")
                err="Minimum Password length must be 4 characters"
        else:
            print('inc')
            err="Incorrect Password!"
        u.save()
    return render(request,'secret/charts.html')

@login_required
def SampleListing(request):
    return render(request, 'secret/tables.html');

@login_required
def SampleReports(request):
    return render(request, 'secret/charts.html');
    
def NotFound(request):
    return render(request, 'secret/404.html');

@login_required
def Logout(request):
    auth.logout(request)
    return redirect('/secret/login/')


