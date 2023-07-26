from django.urls import path, include
from . import views

urlpatterns = [
    path('home/',views.home),
    path('password/', views.password, name = 'password'),
]
