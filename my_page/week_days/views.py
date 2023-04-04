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


# Возвращает главную страницу todo_week
def index(request):
    return render(request, 'week_days/greeting.html')


# Возвращает переадресованный запрос с именем дня + url
def get_info_about_day_number(request, day_num: int):
    if 1 <= day_num <= 7:
        day_name = list(week_days)[day_num - 1]
        redirect_url = reverse('todo-week-name', args=(day_name,))
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound(f'Неверный номер дня - {day_num}')


# Возвращает информацию о дне недели
def get_info_about_day_str(request, day_str: str):
    try:
        return render(request, 'week_days/greeting.html')
        # return HttpResponse(week_days[day_str.lower()])
    except:
        return HttpResponseNotFound('Ты тупой?')
