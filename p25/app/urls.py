from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('insert_school', insert_school, name='insert_school'),
    path('insert_student',insert_student, name='insert_student'),
    path('lists', lists, name='lists'),
    path('display<pk>', display, name='display')
]
