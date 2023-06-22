
from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse
def insert_topic(request):
    tn=input('enter topic_name:')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('Topic data is inserted')

def insert_webpage(request):
    tn=input('enter topic_name:')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('Enter name:')
    u=input('Enter url:')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    return HttpResponse('Topic data is inserted')

def insert_accessrecord(request):
    tn=input('enter topic_name:')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('Enter name:')
    u=input('Enter url:')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    a=input('enter author:')
    d=input('enter date(yyyy-mm-dd):')
    ARO=Access_Record.objects.get_or_create(author=a,name=WO,date=d)[0]
    ARO.save()
    return HttpResponse('accessrecord data is inserted')

def display_topics(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    return render(request,'display_topics.html',d)
def display_webpages(request):
    webpages=Webpage.objects.all()
    d={'webpages':webpages}
    return render(request,'display_webpages.html',d)
def display_accessrecords(request):
    accessrecords=Access_Record.objects.all()
    d={'accessrecords':accessrecords}
    return render(request,'display_accessrecords.html',d)