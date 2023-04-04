from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def get_info_about_word(request, word: str):
    data = {
        'name': word
    }
    return render(request, 'blog/detail_by_name.html', context=data)
    #return HttpResponse(f'Это страница {word}')


def get_info_about_number(reqiest, number: int):
    data = {
        'number': number
    }
    return render(reqiest, 'blog/detail_by_number.html', context=data)
    #return HttpResponse(f'Здесь содержится информация о посте под номером {number}')


def posts(request):
    # data = {
    #     'year_born': 'CONTENT',
    #     'city_born': 'CONTENT',
    #     'movie_name': 'CONTENT'
    # }
    # return render(request, 'blog/test.html', context=data)
    return HttpResponse(f'Это страница posts')


def get_guinness_world_records(request):
    context = {
        'power_man': 'Narve Laeret',
        'bar_name': 'Bob’s BBQ & Grill',
        'count_needle': 1790,
    }
    return render(request, 'blog/guinnessworldrecords.html', context=context)
