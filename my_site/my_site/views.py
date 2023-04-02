from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your views here.
def page_main(reques):
    return HttpResponse(render_to_string('blog/index.html'))
    # return HttpResponse('Главная страница')
