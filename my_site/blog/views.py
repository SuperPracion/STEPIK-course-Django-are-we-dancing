from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def get_info_about_word(request, word: str):
    return HttpResponse(f'Это страница {word}')


def get_info_about_number(reqiest, number: int):
    return HttpResponse(f'Здесь содержится информация о посте под номером {number}')


def posts(request):
    return render(request, 'blog/list_detail.html')
    #return HttpResponse(f'Это страница posts')
