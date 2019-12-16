from django.shortcuts import render, redirect

from django.contrib import messages
from question import forms

from main import models
    
def login(request):
    # print(request.__dict__)
    if request.method == "POST":
        # print(request._post.get('password'))
        messages.success(request, 'Thx for coming back, bro!')
        return redirect("index")
    return render(request, "author/authorize.html", {'form':forms.LoginForm()})

def reg(request):
    print(request)
    # print(request.__dict__)
    if request.method == "POST":
        # print(request._post.get('password'))
        messages.success(request, 'Thx for registration here, bro!')
        return redirect("index")
    return render(request, "author/reg.html", {'form':forms.RegForm()})