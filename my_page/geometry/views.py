from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from math import pi


# Возвращает главную страницу приложения
def geometry_page(request):
    return HttpResponse('rectangle/ или square/ или circle/')


# Производит расчёты площади прямоугольника
def get_rectangle_area(request, width: int, height: int):
    return render(request, 'geometry/rectangle.html')
    # if 'get_' in request.path:
    #     redirect_url = reverse('rectangle-root', args=(width, height,))
    #     return HttpResponseRedirect(redirect_url)
    # return HttpResponse(f'Площадь прямоугольника {width}x{height} равна {width * height}')

# Производит расчёт площади квадрата
def get_square_area(request, width):
    return render(request, 'geometry/square.html')
    # if 'get_' in request.path:
    #     redirect_url = reverse('square-root', args=(width,))
    #     return HttpResponseRedirect(redirect_url)
    # return HttpResponse(f'Площадь квадрата {width}x{width} равна {width * width}')


# Производит расчёт площади круга
def get_circle_area(request, radius):
    return render(request, 'geometry/circle.html')
    # if 'get_' in request.path_info:
    #     redirect_url = reverse('circle-root', args=(radius,))
    #     return HttpResponseRedirect(redirect_url)
    # return HttpResponse(f'Площадь круга {radius} равна {pi * radius * radius}')