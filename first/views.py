from django.shortcuts import render, redirect, HttpResponse
from django.contrib import auth

def loginPage(request):
    context = {}
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(email=username, password=password)
        if user is not None:
            auth.login(request, user)
            print(user.groups.all())
            if (user.groups.all()[0].name == 'Companies'):
                return redirect('company/')
            elif (user.groups.all()[0].name == 'Clients'):
                return redirect('shop/')
            elif (user.groups.all()[0].name == 'Admins'):
                return redirect('admin/')
            else:
                return redirect('/')
        else:
            context['login_error'] = True
            return render(request, 'first/login.html', context)
    else:
        context['login_error'] = False
        return render(request, 'first/login.html', context)

def signPage(request):
    context = {}
    return render(request, 'first/sign.html', context)