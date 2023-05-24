from django.shortcuts import render

# Create your views here.

from app.models import *
from django.http import HttpResponse

def topic_insert(request):

    tn=input('enter topic_name ')

    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()

    return HttpResponse('Topic name is inserted successfully')


def web_insert(request):

    tn=input('enter topic_name ')

    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()

    n=input('enter name ')
    e=input('enter email ')

    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,email=e)[0]
    WO.save()

    return HttpResponse('Webpage is inserted successfully')

def access_insert(request):
    
    tn=input('enter topic_name ')

    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()

    n=input('enter name : ')
    e=input('enter email ')

    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,email=e)[0]
    WO.save()
    
    a=input('enter author : ')
    url=input('enter url : ')

    AO=Access.objects.get_or_create(name=WO,author=a,url=url)[0]
    AO.save()

    return HttpResponse('Acces page is inserted succesfully')