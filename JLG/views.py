from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html',context={'index':index})

def register(request):
    if request.method == 'GET':
        return  render(request,'register.html')
    elif request.method == 'POST':
        print(request.POST)
        user = User()
        user.username = request.POST.get('username')
        user.password = request.POST.get('password')
        user.passwords = request.POST.get('passwords')
        user.save()

    return HttpResponse('正在注册')

def entry(request):
    return render(request,'entry.html',context={'entry':entry})

