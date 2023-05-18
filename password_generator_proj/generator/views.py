import random

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'generator/home.html')

def password(request):


    characters = list('abcdefghijklmnopqrstuvwxyz')

    lenght = int(request.GET.get('length', 12))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIGKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    if request.GET.get('special'):
        characters.extend(list('!.,$@*&?#№'))

    thepassword = ''
    for elem in range(lenght):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})


