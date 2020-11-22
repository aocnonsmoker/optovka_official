from django.shortcuts import render

def mainPage(request):
    context = {}
    return render(request, 'company/main.html', context)
