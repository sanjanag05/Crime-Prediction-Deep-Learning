from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('streamLive', include('core.urls')),
    path('register', views.register, name="register"),
    path('crimerate', views.crimerate, name="crimerate"),
    path('login', views.login, name="login"),
    path('send_sos_signal/', views.send_sos_signal, name='send_sos_signal')
]

