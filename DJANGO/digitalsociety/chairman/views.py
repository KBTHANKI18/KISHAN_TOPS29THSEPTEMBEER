from django.shortcuts import render
from . models import *
"""
ORM : OBJECT RELATIONAL MAPPER

==> retrieve single data condition wise from the model using of get() 
      User.objects.get(fieldname = value)
"""
# Create your views here.

def home(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
    if uid.role == "Chairman":
            cid = Chairman.objects.get(user_id = uid)
            context = {
                'uid' : uid,
                'cid' : cid,
            }
            return render(request,"chairman/index.html",context)
    else:
        return render(request,"Chairman/login.html")
    

def login(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "Chairman":
            cid = Chairman.objects.get(user_id = uid)
            context = {
                'uid' : uid,
                'cid' : cid,
            }
            return render(request,"chairman/index.html",context)
        else:
            pass

    if request.POST:
        print("===> Login Form Submitted")
        p_email = request.POST['email']
        p_password = request.POST['password']
        
        try:
            uid = User.objects.get(email = p_email)

            if uid.password == p_password:
                if uid.role == "Chairman":
                    cid = Chairman.objects.get(user_id = uid)
                    print("===> First Name : ",cid.firstname)

                    request.session['email'] = uid.email
                    context = {
                        "uid" : uid,
                        "cid" : cid,
                    }

                    return render(request,"chairman/index.html",context)
                else:
                    sid = Chairman.objects.get(user_id = uid)
            else:
                msg = "Invalid Password"
                context = {
                    "msg" : msg,
                }
                return render(request,"chairman/login.html",context)

            #print("===>Resonse : ",uid)
            #print("===> email = ",p_email)
            #print("===> password = ",p_password)
        except: 
            msg = " Invalid Email or Password"
            context = {
                "msg" : msg
            }
            return render(request,"chairman/login.html",context)      
    
    else:
        print("===> Login Form Page Refresh")

    return render(request,"chairman/login.html")

def logout(request):
    if "email" in request.session:
        del request.session['email']
        return render(request,"chairman/login.html")
    else:
        return render(request,"chairman/login.html")