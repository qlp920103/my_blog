from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse(u"myblog 对对对")

def sum_t(request):
    pass