from django.shortcuts import render, redirect,reverse
from  django.http import HttpResponseRedirect
from .models import ChatBox
from . forms import ChatBoxForm
from SocialCred.models import UserInfo, User
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

def chatbox(request):
    return render(request, "chat/Chat.html", {})
@csrf_exempt
def send(request, username):
    form = ChatBoxForm()
    uid = User.objects.get(username=username)
    u = UserInfo.objects.get(usr=uid)
    m = UserInfo.objects.get(usr=request.user)
    chat = ChatBox.objects.filter(Q(sender=m, receiver=u) | Q(receiver=m, sender=u))

    dic = {"chat": chat, "rec": u, "m": m}
    if request.method == "POST":
        message = request.POST['message']
        chatb = ChatBox(sender=m, receiver=u, message=message)
        chatb.save()
        return redirect("ChatApp:send", username=username)
    return render(request, "chat/Chat.html", dic)