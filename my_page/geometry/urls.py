from django.urls import path
from . import views

urlpatterns = [
    path('', views.geometry_page),
    path(f'rectangle/<int:width>/<int:height>', views.get_rectangle_area, name='rectangle-root'),
    path(f'square/<int:width>', views.get_square_area, name='square-root'),
    path(f'circle/<int:radius>', views.get_circle_area, name='circle-root'),

    path(f'get_rectangle_area/<int:width>/<int:height>', views.get_rectangle_area),
    path(f'get_square_area/<int:width>', views.get_square_area),
    path(f'get_circle_area/<int:radius>', views.get_circle_area),
]
