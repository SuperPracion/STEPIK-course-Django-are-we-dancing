from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),

    path('type/', views.get_info_about_types),
    path('type/<str:type_name>', views.get_info_about_type, name='type-name'),

    path('<int:sign_zodiac>/', views.get_info_about_zodiac_sign_by_number),
    path('<str:sign_zodiac>/', views.get_info_about_zodiac_sign, name='horoscope-name'),
]

