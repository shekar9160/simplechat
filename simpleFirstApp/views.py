from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def FirstPageController(request):
    return HttpResponse("<h1>My First Django Project Page</h1>")

def IndexPageController(request):
    return HttpResponse("<h1>This is Index Page</h1>")

def HtmlPageController(request):
    return render(request,"htmlpage.html")

def HtmlPageControllerWithData(request):
    data1="This is Data 1 Passing to HTML Page"
    data2="This is Data 2 Passing to HTML Page"
    return render(request,"htmlpage_with_data.html",{'data':data1,'data1':data2})

def PassingDatatoController(request,url_data):
    return HttpResponse("<h2>This is Data Coming Via URL : "+url_data)