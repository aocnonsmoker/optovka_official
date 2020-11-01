from django.shortcuts import render, redirect
from django.contrib import auth

def loginPage(request):
    context = {}
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            context['login_error'] = 'Something wrong'
            return render(request, 'first/login.html', context)
    else:
        return render(request, 'first/login.html', context)