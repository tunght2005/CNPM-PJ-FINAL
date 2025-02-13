from django.urls import path
from . import  views

urlpatterns = [
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register'),
    path('forgot/',views.forgot, name='forgot'),
    #path('', views.home, name='home'),
]
