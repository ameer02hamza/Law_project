from django.shortcuts import render, HttpResponse, HttpResponseRedirect,reverse
from SocialCred.models import UserInfo
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from Appointment.models import notify
from django.db.models import Q
from .models import rating


def listing(request):
    lawyer = UserInfo.objects.all().filter(usrtype=True).exclude(usr=request.user)
    paginator = Paginator(lawyer, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    us = request.user
    lyr = UserInfo.objects.all()
    ntest =notify.objects.filter(Q(NfL=True, frm__lawyer=request.user) | Q(NfC=True, frm__client=request.user))
    dic = {"pageobj": page_obj, "law": lyr, "user": us, "noti": ntest}

    return render(request, "LawyerListing/lawyerlistings.html", dic)

def slisting(request, id):
    print(id, " udrt")
    rat = rating.objects.filter(RoL=id).order_by("-id")
    r=0
    for i in rat:
        print(i.ratings)
        r = r+i.ratings

    try:
        trate =r/rat.count()
    except ZeroDivisionError:
        trate = 0
    print("rate ", trate)
    lawyer = UserInfo.objects.get(usr=id)
    lyr = UserInfo.objects.all()
    print(lawyer.usr.id)
    ntest =notify.objects.filter(Q(NfL=True, frm__lawyer=request.user) | Q(NfC=True, frm__client=request.user))
    if request.method == "POST":
        ratng = float(request.POST["check"])
        review = request.POST['review']
        print(ratng, review, request.user,id)
        inst = User.objects.get(id=id)
        rtng = rating(ratings=ratng,review=review,RoL=inst, RC=request.user)
        rtng.save()
        return HttpResponseRedirect(reverse("lawyer:SLawyerlist", args=[id]))
    paginator = Paginator(rat, 4)
    pagenumber = request.GET.get('page')
    page_obj = paginator.get_page(pagenumber)
    r = rating.objects.filter(RoL=id, RC=request.user)
    dic = {"lawyer": lawyer, "law": lyr, "noti": ntest, "rating": trate, "rtng":page_obj, "r": r}
    return render(request, "LawyerListing/singlelawyer.html", dic)

def urat(request, id):
    rat = rating.objects.get(id=id)
    if request.method == "POST":
        r = request.POST['check']
        rev = request.POST['review']
        rat.ratings = r
        rat.review = rev
        return HttpResponseRedirect(reverse("lawyer:SLawyerlist",args=[rat.RoL.id]))
    return render(request, "Master/editrating.html", {"rat": rat})    
            

        




