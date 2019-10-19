from django.shortcuts import render

# Create your views here.

def index(request, year=0):
    context = {"test":"roar", 
        "questions" :
            [{'name':1}, 
            {'name':2}]}
    return render(request, "main/index.html", context)

def tags(request):
    return render(request, "main/tags.html", {})

def settings(request):
    return render(request, "main/settings.html", {})


    #return HttpResponse('some_text')#content-type="text/plain"