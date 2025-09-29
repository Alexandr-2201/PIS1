from django.shortcuts import render
from django.http import HttpResponse
from django import template


def hello(request):
    return HttpResponse(u'Привет, Мир!', content_type="text/plain; charset=utf-8")
def home(request):
    return render(request, 'templates/index.html')
def modern(request):
    return render(request, 'templates/static_handler.html')

# Create your views here.
