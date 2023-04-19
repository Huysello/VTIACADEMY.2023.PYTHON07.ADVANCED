from django.urls import path
from .views import car_list, car_detail, car_create, car_update, car_delete

urlpatterns = [
    path('', car_list, name='car_list'),
    path('<int:pk>/', car_detail, name='car_detail'),
    path('create/', car_create, name='car_create'),
    path('<int:pk>/update/', car_update, name='car_update'),
    path('<int:pk>/delete/', car_delete, name='car_delete'),
]
