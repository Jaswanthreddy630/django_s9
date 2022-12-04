from django.core.checks import messages
from django.shortcuts import render, loader, redirect
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.models import User,auth


def index(request):
    return render(request,"index.html")
def register(request):
    return render(request,"registration.html")
def login(request):
    return render(request,"login.html")
# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(username=username,password=password)
#         if user is not None:
#             auth.login(request,user)
#             return redirect('/')
#         else:
#             return HttpResponseRedirect(reverse('login'))
#     else:
#         return render(request,'login.html')

def contactus(request):
    return render(request,"contact.html")
def about(request):
    return render(request,"about.html")
def module(request):
    return render(request,"module.html")
def module11(request):
    return render(request,"module11.html")
def profiles(request):
    return render(request,"profiles.html")
# Create your views here.
def index1(request):
	return HttpResponse('Welcome to Django')
def templateexample(request):
    template=loader.get_template('first.html')
    return HttpResponse(template.render())
def templatecontext(request):
    context={'name':'abc'}
    return render(request,'second.html',context)
def urlparams(request,num1,num2):
	n1=int(num1)
	n2=int(num2)
	context={'a' : n1,'b' : n2,'c' : n1+n2}
	return render(request,'third.html',context)

# def insert(request):
#     if request.method == 'POST':
#         a = request.POST['username']
#       # b = request.POST['fname']      # c = request.POST['lname']
#         d = request.POST['user_mail']
#         e = request.POST['password1']
#         f = request.POST['pass2']
#         if e==f:
#             if User.objects.filter(username=a).exists():
#                 messages.error(request,"Username Taken")
#                 return HttpResponseRedirect(reverse('register'))
#             elif User.objects.filter(email=d).exists():
#                 messages.error(request,"Email exists")
#                 return HttpResponseRedirect(reverse('register'))
#             else:
#                 user = User.objects.create_user(username = a, password = e, email = d )
#                 user.save()
#                 return HttpResponseRedirect(reverse('login'))
#     else:
#         return render(request,'registration.html')