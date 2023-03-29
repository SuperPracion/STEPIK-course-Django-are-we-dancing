from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
def get_info_about_week_day(request, week_day):
    week_days = {
        'monday': "Страницы Понедельника",
        'tuesday': "Страница Вторника"
    }

    try:
        return HttpResponse(week_days[week_day.lower()])
    except:
        return HttpResponseNotFound('Ты тупой?')
