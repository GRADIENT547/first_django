from django.shortcuts import render

def index(request):
    return render(request, 'testapp/index.html')

def hi(request):
    return render(request, 'testapp/hi.html')