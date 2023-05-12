
from django.urls import path, re_path, include

urlpatterns = [
    re_path('api/', include('todo.api.urls')),
]