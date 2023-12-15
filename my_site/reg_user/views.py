from django.shortcuts import render, HttpResponse


def reg(request):
    
    return render(request, 'registration/reg.html')
