from django.shortcuts import render, redirect
from SocialCred.models import UserInfo
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from Blog.models import AddBlog
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.views.generic import ListView
def lawyer(request):
    if "term" in request.GET:
        law = request.GET.get('term')
        spclty = UserInfo.objects.filter(Q(speciality__icontains=law))
        loc = UserInfo.objects.filter(Q(address__icontains=law))
        fname = UserInfo.objects.filter(Q(usr__first_name__icontains=law, usr__last_name__icontains=law))
        lyr = list()
        for lawyer in spclty:
            lyr.append(lawyer.speciality)
        for lawyer in fname:
            lyr.append(lawyer.usr.first_name)
        for lawyer in loc:
            lyr.append(lawyer.address)
        return JsonResponse(lyr, safe=False)

    return render(request, "searchmodule.html")

def blog(request):
    if "term" in request.GET:
        law = request.GET.get('term')
        spclty = AddBlog.objects.filter(Q(btext__icontains=law) | Q(btitle__icontains=law))
        lyr = list()
        for lawyer in spclty:
            lyr.append(lawyer.btitle)
        return JsonResponse(lyr, safe=False)
    return render(request, "searchblog.html")

def searchlaw(request):
    lawtype = str(request.GET.get('type'))
    loc = str(request.GET.get('loc'))
    lawyer = UserInfo.objects.filter(Q(speciality__icontains=lawtype.upper(), address__icontains=loc.upper()) |
                                     Q(usr__first_name__icontains=lawtype), Q(address__icontains=loc.upper()))
    print(lawyer)
    paginator = Paginator(lawyer, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    us = request.user
    lyr = UserInfo.objects.all()

    dic = {"pageobj": page_obj, "law": lyr, "user": us}

    return render(request, "LawyerListing/searchlaw.html", dic)

def blores(request):
    bg = request.GET.get('blog')
    blogs = AddBlog.objects.filter(Q(btitle__icontains=bg, btext__icontains=bg) | Q(btext__icontains=bg))
    paginator = Paginator(blogs, 2)
    pagenumber = request.GET.get('page')
    page_obj = paginator.get_page(pagenumber)
    dic = {"blog": page_obj}
    return render(request, "Blogs&Questions/myblog.html", dic)





