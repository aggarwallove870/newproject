from django.shortcuts import redirect
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.auth.models import User
from django.contrib.auth import logout
class UserLogoutAfterPasswordMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def callback(self, sender, *kwargs):
        self.body_text = kwargs.pop('msg')

    def __call__(self, request):
        pass
        # check=request.session.get('opwd')
        # print(check)
        # print("Here session",request.session.get("is_chnaged"),request.session.keys())
        if request.session.get("is_chnaged") == "Changed sucessully":
            del request.session['is_chnaged']
            logout(request)
            
        
        # if request.method == "POST":
        #     old = request.POST.get('opwd')
        #     print(old)
        #     new=request.POST.get('npwd')
        #     print(new)
        #     cpwd=request.POST.get('cnpwd')
        #     print(cpwd)
        #     print(request.POST.values)
        #     if old != new and new==cpwd:
        #         logout(request)
        #         print ("logout succesfully")
             
        return self.get_response(request)



    
        


