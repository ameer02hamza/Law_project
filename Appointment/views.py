from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import AppointmentForm, notify
from SocialCred.models import UserInfo

# Create your views here.
def aform(request, id):
    print(id)
    uid = User.objects.get(id=id)
    cid = request.user
    lyr = UserInfo.objects.all()
    ntest = notify.objects.filter(Q(NfL=True, frm__lawyer=request.user) | Q(NfC=True, frm__client=request.user))
    if request.method == "POST":
        fname = request.POST['fname']
        email = request.POST['email']
        phnumber = request.POST['pno']
        casedetails = request.POST['casedet']
        adate = request.POST['adate']
        atime = request.POST['atime']
        print(fname, email, phnumber, casedetails, adate, atime)
        form = AppointmentForm(Name=fname, email=email, Phone_no=phnumber, case_details=casedetails,
                               adate=adate, atime=atime, client=cid)
        form.save()
        fid = AppointmentForm.objects.get(id=form.id)
        print("idd ", fid)
        noti = notify(frm=fid)
        noti.save()
        form.lawyer.add(uid)
        return redirect("Appointment:status")
    return render(request, "Appointments/Appointmentform.html", {"user": uid, "law": lyr, "noti": ntest})

def status(request):
    obj = AppointmentForm.objects.filter(client=request.user).order_by("-id")
    lawyer = UserInfo.objects.all()
    ntest =notify.objects.filter(Q(NfL=True, frm__lawyer=request.user) | Q(NfC=True, frm__client=request.user))
    return render(request, "Appointments/appointstatus.html", {"appointment": obj, "law": lawyer, "noti": ntest})

def apprequest(request):
    if request.method == "POST":
        uid = request.POST['id']
        adate = request.POST['adate']
        atime = request.POST['atime']
        print(uid, adate, atime)
        i = AppointmentForm.objects.get(id=uid)
        i.adate = adate
        i.atime = atime
        i.status = "Confirmed"
        i.save()
        req = AppointmentForm.objects.get(id=i.id)
        print("req", req.id)
        test = notify.objects.get(frm__id=req.id)

        print(test, "this is test")
        test.msg = "Your Appointment Has been confirmed"
        test.NfL = False
        test.NfC = True
        test.save()
    app = AppointmentForm.objects.all().filter(lawyer=request.user, status="pending")
    lyr = UserInfo.objects.all()
    ntest =notify.objects.filter(Q(NfL=True, frm__lawyer=request.user) | Q(NfC=True, frm__client=request.user))
    return render(request, "Appointments/ConfimAppointment.html", {"Appoint": app, "law": lyr, "noti": ntest})

def reject(request, id):
    i = AppointmentForm.objects.get(id=id)
    i.status="Rejected"
    i.save()
    noti =notify.objects.get(frm__id=i.id)
    noti.NfL=False
    noti.NfC=True
    noti.msg="Your Appointment has been rejected"
    noti.save()
    return HttpResponseRedirect(reverse("Appointment:arequests"))

def confirmed(request, id):
    i = AppointmentForm.objects.get(id=id)
    i.status = "Confirmed"
    i.save()
    noti = notify.objects.get(frm__id=i.id)
    noti.NfL = False
    noti.NfC = True
    noti.msg = "Your Appointment has been confirmed"
    noti.save()
    return HttpResponseRedirect(reverse("Appointment:arequests"))

def test(request):
    print(request.user)
    obj = AppointmentForm.objects.filter(client=request.user).order_by("-id")
    lyr = list()
    for l in obj:
        for p in l.lawyer.all():
            lyr.append(p.first_name)
    return JsonResponse({"apps": list(obj.values()), "name": lyr})

def appointnoti(request):
    ntest = notify.objects.filter(Q(NfL=True, frm__lawyer=request.user) | Q(NfC=True, frm__client=request.user)).order_by("-id")
    return JsonResponse({"noti": list(ntest.values())})

def notiend(request,id):
    notification = notify.objects.get(id=id)
    notification.NfC = False
    notification.save()
    print("done")
    return HttpResponseRedirect(reverse("Appointment:status"))