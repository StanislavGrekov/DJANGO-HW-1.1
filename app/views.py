from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
import os

def home_view(request):
    template_name = 'app/home.html'

    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('current'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    template_name = 'app/current_time.html'
    current_time = datetime.now()
    msg = f'Текущее время: {current_time}'
    return render(request, template_name, context = {'msg': msg})


def workdir_view(request):
    list_containing = os.listdir()
    for_view = []
    for element in list_containing:
        new_element = element + '__'
        for_view.append(new_element)
    return HttpResponse(for_view)
