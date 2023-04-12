from django.urls import path
from . import views
from .views import person_list

urlpatterns = [
    path('', views.index, name='index'),
    path('persons/', person_list, name='person_list'),
]
