from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_guinness_world_records),
    path('<int:number>/', views.get_info_about_number),
    path('<str:word>/', views.get_info_about_word),
]
