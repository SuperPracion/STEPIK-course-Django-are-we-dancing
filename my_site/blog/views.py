from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def get_info_about_request(request, name_post):
    return HttpResponse(f'Это страница {name_post}')


def posts(request):
    return HttpResponse(f'Это страница posts')
