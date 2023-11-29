from django.urls import path
from . import views

urlpatterns = [
    path('', views.send_file, name="home-page"),
    path('runtext/', views.send_file, name="send-file"),
]