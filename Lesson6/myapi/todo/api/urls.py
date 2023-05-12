from django.urls import re_path, path, include
from .views import (
    TodoListApiView,
    TodoDetailApiView
)

urlpatterns =[
    re_path('', TodoListApiView.as_view()),
    re_path('<int:todo_id>/', TodoDetailApiView.as_view()),
]
