from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def Test(request):
    return render(request, 'home.html', {'navbar':'home'})


def contact(request):
    return render(request, 'Tes.html', {'navbar':'contact'})


def about(request):
    return render(request, 'about.html', {'navbar':'about'})
