from django.shortcuts import render

# Create your views here.

def reg(request):
    return render(request, "author/reg.html", {})
    
def login(request):
    return render(request, "author/authorize.html", {})