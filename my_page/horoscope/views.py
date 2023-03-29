from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
def get_info_about_zodiac_side(request, side_zodiac):
    sides = {
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

    try:
        return HttpResponse(sides[side_zodiac])
    except:
        return HttpResponseNotFound('Ты чо несёшь?')

    # if side_zodiac in sides:
    #     return HttpResponse(sides[side_zodiac])
    # else:
    #     return HttpResponseNotFound('Ты чо несёшь?')
