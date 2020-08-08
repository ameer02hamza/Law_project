from django.shortcuts import render,redirect, reverse
from django.views.generic import (CreateView,UpdateView,DetailView,
                                  ListView,DeleteView)
from . models import Question
from . forms import QuesForm
from django.views.decorators.csrf import csrf_exempt
from SocialCred.models import UserInfo
from django.contrib.auth.models import User
from Appointment.models import notify
from django.db.models import Q, Case, When
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from Lawyers.models import rating


class ArticleListView(ListView):
    template_name = "Blogs&Questions/quedet.html"

    def get_queryset(self):
        queryset = Question.objects.all().order_by("-id")
        return queryset

    def get(self, request, *args, **kwargs):
        lyr = UserInfo.objects.all()
        data = self.get_queryset()
        paginator = Paginator(data, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        ntest = notify.objects.filter(Q(NfL=True, frm__lawyer=request.user) | Q(NfC=True, frm__client=request.user))
        dic = {"law": lyr, "object_list": page_obj, "noti": ntest}
        return render(request, self.template_name, dic)



class AskQuestion(CreateView):
    template_name = "Blogs&Questions/askquest.html"

    @csrf_exempt
    def get(self, request, *args, **kwargs):
        form = QuesForm()
        ntest = notify.objects.filter(Q(NfL=True, frm__lawyer=request.user) | Q(NfC=True, frm__client=request.user))
        context = {"form": form, "noti": ntest}
        return render(request, self.template_name, context)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        u = User.objects.get(id=request.user.id)
        print(u.id,"hij")
        ins = UserInfo.objects.get(usr=u)
        print(ins.id," if")
        form = QuesForm(request.POST)
        if form.is_valid():

            print(form.cleaned_data)
            print(form.cleaned_data," dataaa")
            foo =form.save(commit=False)
            print(foo," foo")
            foo.uprof = ins
            foo.save()

        ntest = notify.objects.filter(Q(NfL=True, frm__lawyer=request.user) | Q(NfC=True, frm__client=request.user))
        context = {"form": form, "noti": ntest}
        # return render(request, self.template_name, context)
        return redirect("Questionaire:lists")

# class Questiondet(CreateView):
#     template_name = "Blogs&Questions/Questionaire.html"
#     form_class = QuesForm
#     queryset = Questions.objects.all()
#
#     def form_valid(self, form):
#         print(form.cleaned_data)
#         return super().form_valid(form)
#
# class Questionupdate(UpdateView):
#     template_name = "Blogs&Questions/Questionaire.html"
#     form_class = QuesForm
#     queryset = Questions.objects.all()
#
#     def get_object(self):
#         id = self.kwargs.get("id")
#         return get_object_or_404(Questions, id=id)
#
#     def form_valid(self, form):
#         print(form.cleaned_data)
#         return super().form_valid(form)

class updateque(UpdateView):
    template_name = "Blogs&Questions/updatequest.html"
    form_class = QuesForm
    queryset = Question.objects.all()


    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Question, id=id)
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    def get_success_url(self):
        return reverse("Questionaire:lists")