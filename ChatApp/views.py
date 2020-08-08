from django.shortcuts import render, redirect,reverse
from  django.http import HttpResponseRedirect
from .models import ChatBox
from . forms import ChatBoxForm
from SocialCred.models import UserInfo, User
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

def chatbox(request):
    m = UserInfo.objects.get(usr=request.user)
    friends = ChatBox.objects.filter(Q(sender=m)).distinct('receiver')
    frequest = ChatBox.objects.filter(Q(receiver=m)).distinct('sender')
    f = ChatBox.objects.filter(Q(receiver=m)).distinct('sender')
    for f in friends:
        print(f.receiver.usr.first_name, "name")
    dic = {"friends": friends, "m": m, "frequest": frequest, "f": f}
    return render(request, "chat/Chat.html", dic)
@csrf_exempt
def send(request, username):
    form = ChatBoxForm()
    uid = User.objects.get(username=username)
    u = UserInfo.objects.get(usr=uid)
    m = UserInfo.objects.get(usr=request.user)
    friends = ChatBox.objects.filter(Q(sender=m)).distinct('receiver')
    f = ChatBox.objects.filter(Q(receiver=m)).distinct('sender')
    chat = ChatBox.objects.filter(Q(sender=m, receiver=u) | Q(receiver=m, sender=u))

    dic = {"chat": chat, "rec": u, "m": m, "friends": friends, "f": f}
    if request.method == "POST":
        message = request.POST['message']
        chatb = ChatBox(sender=m, receiver=u, message=message)
        chatb.save()
        return redirect("ChatApp:send", username=username)
    return render(request, "chat/Chat.html", dic)