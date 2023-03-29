from django.urls import path
from . import views

urlpatterns = [
    path(f'<week_day>/', views.get_info_about_week_day),
]

