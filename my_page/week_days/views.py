from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def monday(request):
    return HttpResponse("Страницы Понедельника")


def tuesday(request):
    return HttpResponse("Страница Вторника")
