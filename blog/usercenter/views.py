from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    print(u"我爱北京天安门")
    return HttpResponse()