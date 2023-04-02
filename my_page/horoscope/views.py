from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

zodiac_dict = {
    'aries': "Aries [ɛəri:z] Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
    'taurus': "Taurus ['tɔ:rəs] Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
    'gemini': "Gemini ['dʒeminai] Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
    'cancer': "Cancer ['kænsə(r)] Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
    'leo': "Leo ['li:əu] Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).",
    'virgo': "Virgo ['vз:gəu] Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
    'libra': "Libra ['li:brə] Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
    'scorpio': "Scorpio ['skɔ:piəu] Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
    'sagittarius': "Sagittarius [sædʒi'tɛəriəs] Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
    'capricorn': "Capricorn ['kæprikɔ:n] Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
    'aquarius': "Aquarius [ə'kwɛəriəs] Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
    'pisces': "['paisi:z] Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)."

}

types = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces'],
}


# Create your views here.
def index(request):
    li_elements = ''
    for sing in zodiac_dict:
        redirect_url = reverse('horoscope-name', args=(sing,))
        li_elements += f'<li><a href={redirect_url}>{sing}</a></li>'

    response = f'<ul>{li_elements}</ul>'

    return HttpResponse(response)


def get_info_about_zodiac_sign(request, sign_zodiac: str):
    try:
        return HttpResponse(render_to_string('horoscope/info_zodiac.html'))
        # return HttpResponse(zodiac_dict[sign_zodiac])
    except:
        return HttpResponseNotFound(f'Ты чо несёшь? {sign_zodiac}')


def get_info_about_zodiac_sign_by_number(request, sign_zodiac: int):
    try:
        redirect_url = reverse('horoscope-name', args=(list(zodiac_dict)[sign_zodiac - 1],))
        return HttpResponseRedirect(redirect_url)
    except:
        return HttpResponseNotFound(f'Ты чо несёшь? 2.0 {sign_zodiac}')


def get_info_about_types(request):
    response = ''
    for type in list(types):
        redirect_url = reverse('type-name', args=(type,))
        response += f'<li><a href={redirect_url}>{type}</a></li>'

    return HttpResponse(response)


def get_info_about_type(request, type_name):
    response = ''
    for sign in types[type_name]:
        redirect_url = reverse('horoscope-name', args=(sign,))
        response += f'<li><a href={redirect_url}>{sign}</a></li>'

    return HttpResponse(response)
