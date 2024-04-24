
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect

from users.models import Users

db = {'s': 's',
      'a': 'a'}


def login(request):
    return render(request, 'users/autorisation_page.html')

def registry(request): #возвращает страничку с регестрацией
    return render(request, 'users/registration.html')

def make_register(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')

    if Users.objects.filter(username=username).exists():
        return render(request, 'users/reg_fall.html')
    user = Users(username=username, email=email, password=password)
    user.save()
    return HttpResponseRedirect('http://127.0.0.1:8000/users/')


def check_info(request): #проверка при авторизации
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        id = Users.objects.get(username=username).id
        password_real = Users.objects.get(username=username).password
        if Users.objects.filter(username=username).exists() and password_real == password:
            return redirect(f'http://127.0.0.1:8000/cabinet/{id}')
        else:
            return render(request, 'users/autorisation_page.html')
    except:
        return render(request, 'users/autorisation_page.html')

