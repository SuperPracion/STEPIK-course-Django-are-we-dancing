from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

week_days = {
    'monday': "Страницы Понедельника",
    'tuesday': "Страница Вторника",
    'wednesday': "Страница Среды",
    'thursday': "Страница Четверга",
    'friday': "Страница Пятницы",
    'saturday': "Страница Субботы",
    'sunday': "Страница Воскресенья",
}


def get_info_about_day(request, day_num: int):
    if 1 <= day_num <= 7:
        day_name = list(week_days)[day_num - 1]
        redirect_url = reverse('todo-week-name', args=(day_name, ))
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound(f'Неверный номер дня - {day_num}')


# Create your views here.
def get_info_about_week_day(request, day_str: str):
    try:
        return HttpResponse(week_days[day_str.lower()])
    except:
        return HttpResponseNotFound('Ты тупой?')
