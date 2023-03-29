from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def page_main(reques):
    return HttpResponse('Главная страница')
