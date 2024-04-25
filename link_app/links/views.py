from datetime import datetime
from rest_framework import viewsets, generics

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView

from . import made_short_link
from users.models import Users
from .models import Links
from .seriallzers import LinkApiSerializer


def cabinet(request, id):
    f = {'id_n' : Users.objects.filter(id=id).first().username, 'id': id}
    return render(request, 'links/cabinet.html', f)


def zapros(request, link):
    a = 'https://' + link
    new_link = Links.objects.filter(short_url=a).first()
    if new_link:
        original_url = new_link.original_url
        parsed_datetime = datetime.now()
        record = Links.objects.get(short_url=a)
        record.last_accessed = parsed_datetime
        record.save()
        return HttpResponseRedirect(original_url)
    else:
        return HttpResponse("Такой ссылки не сущетсвует!")



def show_links(request, id):
    links = []

    links_with_owner_id = Links.objects.filter(owner_id=int(id))
    d = {
        'links': links_with_owner_id
    }
    return render(request, 'links/show_links.html', d)


def make_link(request):
    id = request.POST.get('id')
    spis = made_short_link.made_short_link(request.POST.get('input_text'))
    if Links.objects.filter(original_url=spis[0]).exists():
        return HttpResponseRedirect(f'http://127.0.0.1:8000/cabinet/{id}')
    user = Users.objects.get(id=id)
    link = Links(original_url=spis[0], short_url=spis[1], owner=user)
    link.save()
    return HttpResponseRedirect(f'http://127.0.0.1:8000/cabinet/{id}')

def user_links(request):
    return HttpResponse("Ссылки пользователя")

##############################################api#############
class ApiLinks(generics.RetrieveAPIView):
    queryset = Links.objects.all()
    serializer_class = LinkApiSerializer
    lookup_field = 'owner_id'
