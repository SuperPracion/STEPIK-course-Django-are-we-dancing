from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path(f'<int:day_num>/', views.get_info_about_day_number, name='todo-week-name'),
    # TODO Удалить name='todo-week-name' в path(f'<int:day_num>/', views.get_info_about_day, name='todo-week-name'), - проверить реакцию системы. Выяснить что root
    path(f'<str:day_str>/', views.get_info_about_day_str, name='todo-week-name'),
]

