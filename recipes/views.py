from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'recipes/temp.html', context={
        'name': 'Felipe'
    })


def about(request):
    return render(request, 'me_apague/temp.html')


def contact(request):
    return HttpResponse('CONTATO')


