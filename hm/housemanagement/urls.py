from django.urls import path, re_path, register_converter
from . import views


urlpatterns = [
    path('', views.index, name='home'),  # http://127.0.0.1:8000
    path('about/', views.about, name='about'),
]
