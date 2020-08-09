from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from .models import UserInfo
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST['uname']
        pswd = request.POST['pswd']
        user = auth.authenticate(username=username, password=pswd)
        if user is not None:
                auth.login(request, user)
                u = UserInfo.objects.get(usr=request.user.id)
                utype = u.usrtype
                if utype== True:
                    return redirect("Appointment:arequests")
                elif utype==False:
                    return redirect("Appointment:status")
                else:
                    return redirect("SocialCred:master")

        else:
            return render(request, "Credentials/signin.html", {"usr": "User Name is incorrect"})

    return render(request, "Credentials/signin.html")
def signup(request):
    if request.method=="POST":
        fname= request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        uname=request.POST['uname']
        pswd=request.POST['pswd1']
        cpswd=request.POST['pswd2']
        usrtype = request.POST['usrtype']
        usrprofile = request.FILES['profile']
        address = request.POST['addr']
        spclty = request.POST['spclty']
        aboutyou = request.POST['desc']
        print(fname, lname, email, pswd, uname, cpswd, usrtype, usrprofile, address.upper(), spclty.upper(), aboutyou)

        if pswd==cpswd:
            if User.objects.filter(username=uname).exists():
                return render(request, "Credentials/signup.html", {"uname":" Your user name already exists"})
            elif User.objects.filter(email=email).exists():
                return render(request, "Credentials/signup.html", {"email":"Your email is already exists"})
            else:
                user = User.objects.create_user(username=uname, first_name=fname, last_name=lname, email=email,
                                                password=pswd)
                uid = user.id
                u = User.objects.get(id=uid)
                if usrtype == "client":
                    usrinfo = UserInfo(usrtype=False, profile_picture=usrprofile, usr=u)
                    usrinfo.save()

                else:
                    usrinfo = UserInfo(usrtype=True, profile_picture=usrprofile, usr=u, address=address.upper(),
                                       description=aboutyou, speciality=spclty.upper())
                    usrinfo.save()
                return redirect('SocialCred:login')



    return render(request,"Credentials/signup.html")

# will remove master law from here this is just for testing purpose
def masterlaw(request):
    u = UserInfo.objects.all()
    dic = {"i":u}
    return render(request, "Master/Master.html", dic)

def logout(request):
    auth.logout(request)
    return redirect("SocialCred:login")
