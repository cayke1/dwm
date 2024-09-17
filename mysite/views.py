from django.shortcuts import render

def login(request):
    return render(request, './login/index.html')

def register(request):
    return render(request, './signup/index.html')