from django.urls import path
from . import views

urlpatterns = [
    path('runtext/', views.send_file, name="path-name"),
]