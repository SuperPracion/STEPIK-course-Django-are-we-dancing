from django.urls import path
from . import views

urlpatterns = [
    path('<side_zodiac>/', views.get_info_about_zodiac_side),
]

