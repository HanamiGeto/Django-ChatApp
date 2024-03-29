from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .models import Chat, Message
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.shortcuts import redirect
from django.urls import reverse


@login_required(login_url='/login/')
def index(request):
    if request.method == 'POST':
        print('Received data ' + request.POST['textmessage'])
        myChat = Chat.objects.get(id=1)
        new_message = Message.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=request.user)
        serialized_obj = serializers.serialize('json', [ new_message, ])
        return JsonResponse(serialized_obj[1:-1], safe=False)
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'messages': chatMessages})

def login_view(request):
    redirect = request.GET.get('next')
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            login(request, user)
            return HttpResponseRedirect(request.POST.get('redirect'))
        else:
            return render(request, 'auth/login.html', {'wrongPassword': True, 'redirect': redirect})
    return render(request, 'auth/login.html', {'redirect': redirect})

def register_view(request):
    redirect = request.GET.get('next')
    if request.method == 'POST':
        user = User.objects.create_user(username=request.POST.get('username'),
                                        email=request.POST.get('email'),
                                        password=request.POST.get('password'))
        user.first_name = request.POST.get('username')
        user.save()
        if user:
            # login_view(request)
            return HttpResponseRedirect(request.POST.get('redirect'))
            # return redirect('chat')
            # return HttpResponseRedirect(reverse('app_name:chat'))
            # return HttpResponseRedirect('login/')
            # return HttpResponseRedirect('auth/login.html')
            # render(request, 'chat/index.html', {'redirect': redirect})
    return render(request, 'register/register.html', {'redirect': redirect})

def logout_view(request):
    logout(request)
    redirect = request.GET.get('next')
    if request.method == 'POST':
        login_view
    return render(request, 'auth/login.html', {'redirect': redirect})
    
# messages_filter = {
#     'class_wrote_message': User.is_authenticated and "message-left" or "message-right"
# }