from django.urls import path
from . import views


app_name = 'colors'


urlpatterns = [
    path('create/', views.color_create, name='create')
]