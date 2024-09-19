from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

class LoginView(View):
    def get(self, request):
        context = {'message': ''}
        return render(request, './login/index.html', context)
    def post(self, request):
        user = request.POST.get('usuario', None)
        password = request.POST.get('senha', None)

        auth = authenticate(username=user, password=password)
        if auth is not None:
            if auth.is_active:
                login(request, auth)
                return redirect('/veicles')
            return render(request, './login/index.html', {'message': 'Usuário inativo'})
        return render(request, './login/index.html', {'message': 'Usuário ou senha inválidos'})
        
            

class RegisterView(View):
    def get(self, request):
        context = {'message': ''}
        return render(request, './signup/index.html', context)