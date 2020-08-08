from django.shortcuts import render, redirect, HttpResponse, reverse
from . models import AddBlog
from django.core.paginator import Paginator
from SocialCred.models import UserInfo
from Appointment.models import notify
from django.db.models import Q
from django.views.generic import (UpdateView)
from Questionaire.forms import QuesForm
from django.shortcuts import get_object_or_404

def sblog(request, id):
    b = AddBlog.objects.get(id=id)
    lyr = UserInfo.objects.all()
    ntest =notify.objects.filter(Q(NfL=True, frm__lawyer=request.user) | Q(NfC=True, frm__client=request.user))

    data = {"blog": b,"law":lyr, "noti":ntest}
    return render(request, "Blogs&Questions/blogdetail.html", data)


def bloglist(request):
    blogs = AddBlog.objects.all()
    paginator = Paginator(blogs, 2)
    pagenumber = request.GET.get('page')
    page_obj = paginator.get_page(pagenumber)
    lyr = UserInfo.objects.all()
    ntest =notify.objects.filter(Q(NfL=True, frm__lawyer=request.user) | Q(NfC=True, frm__client=request.user))

    dic = {"blog": page_obj, "law":lyr, "noti":ntest}
    return render(request, "Blogs&Questions/myblog.html", dic)

def addblog(request):
    lyr = UserInfo.objects.all()
    us = request.user
    ntest =notify.objects.filter(Q(NfL=True, frm__lawyer=request.user) | Q(NfC=True, frm__client=request.user))

    if request.method =="POST":
        btitle = request.POST['title']
        pic = request.FILES['profil']
        blog = request.POST.get('blog')
        u = request.user
        print("prof ",pic)
        b = AddBlog(btitle=btitle, bpic=pic, btext=blog, postedby=u)
        b.save()
        return redirect('Blog:myblog')

    return render(request,"Blogs&Questions/addblog.html", {"law": lyr, "user": us, "noti":ntest})

def myblog(request):
    lyr = UserInfo.objects.all()
    u = request.user
    blogs = AddBlog.objects.all().filter(postedby=u)
    paginator = Paginator(blogs, 2)
    pagenumber = request.GET.get('page')
    page_obj = paginator.get_page(pagenumber)
    ntest =notify.objects.filter(Q(NfL=True, frm__lawyer=request.user) | Q(NfC=True, frm__client=request.user))
    dic = {"blog": page_obj, "law":lyr, "noti": ntest}
    return render(request, "Blogs&Questions/myblog.html", dic)


def updateblog(request, id):
    ublog = AddBlog.objects.get(id=id)

    if request.method == "POST":
        title = request.POST['title']
        blog = request.POST['blog']
        ublog.btitle= title
        ublog.btext =blog
        ublog.save()
        return redirect("Blog:myblog")

    return render(request, "Blogs&Questions/updateblog.html", {"blog": ublog})