from django.urls import path
from .views import (
    home,
    register,
    register_api,
)

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('register_api/', register_api, name='register_api'),
]