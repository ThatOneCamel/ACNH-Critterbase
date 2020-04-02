from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from .models import Fish, Insect

# Create your views here.
def index(request):
    return HttpResponse("index")

def fishAll(request):
    fish_list = Fish.objects.all()
    output = []
    for f in fish_list:
        output.append(f.name)
    return JsonResponse(output,safe=False)

def fish(request,name):
    if "%20" in name:
        name = name.replace("%20"," ")
    if "%2520" in name:
        name = name.replace("%2520"," ")
    f = Fish.objects.get(name=name)
    nMonths = []
    sMonths = []
    for n in f.northmonth_set.all():
        nMonths.append(n.name)
    for s in f.southmonth_set.all():
        sMonths.append(s.name)
    output = {'name':f.name, 'time':f.timeframe, 'location':f.location, 'shadow':f.shadow,'price':f.price, 'Northern Hemisphere':nMonths, 'Southern Hemisphere':sMonths}
    print(output)
    return JsonResponse(output)

def insectAll(request):
    insect_list = Insect.objects.all()
    output = []
    for i in insect_list:
        output.append(i.name)
    return JsonResponse(output,safe=False)
def insect(request,name):
    if "%20" in name:
        name = name.replace("%20"," ")
    if "%2520" in name:
        name = name.replace("%2520"," ")
    i = Insect.objects.get(name=name)
    nMonths = []
    sMonths = []
    for n in i.northmonth_set.all():
        nMonths.append(n.name)
    for s in i.southmonth_set.all():
        sMonths.append(s.name)
    output = {'name':i.name, 'time':i.timeframe, 'location':i.location, 'price':i.price, 'Northern Hemisphere':nMonths, 'Southern Hemisphere':sMonths}
    print(output)
    return JsonResponse(output)

def north(request, name):
    return HttpResponse("You're looking at month: %s in the northern hemisphere." % name)

def south(request, name):
    return HttpResponse("You're looking at month: %s in the southern hemisphere." % name)