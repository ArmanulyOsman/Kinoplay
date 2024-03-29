from django.urls import path
from mainapp.views import *


urlpatterns = [
    path('', index, name='index'),
    path('director/<int:id>/', director, name='director'),
    path('show/<int:id>/', show, name='show'),
]
