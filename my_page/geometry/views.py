from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from math import pi


# Create your views here.
def geometry_page(request):
    return HttpResponse('rectangle/ или square/ или circle/')


def get_rectangle_area(request, width: int, height: int):
    if 'get_' in request.path:
        redirect_url = reverse('rectangle-root', args=(width, height, ))
        return HttpResponseRedirect(redirect_url)
    return HttpResponse(f'Площадь прямоугольника {width}x{height} равна {width * height}')


def get_square_area(request, width):
    if 'get_' in request.path:
        redirect_url = reverse('square-root', args=(width, ))
        return HttpResponseRedirect(redirect_url)
    return HttpResponse(f'Площадь квадрата {width}x{width} равна {width * width}')


def get_circle_area(request, radius):
    if 'get_' in request.path_info:
        redirect_url = reverse('circle-root', args=(radius, ))
        return HttpResponseRedirect(redirect_url)
    return HttpResponse(f'Площадь круга {radius} равна {pi * radius * radius}')
