from django.urls import path
from . import  views
from .views import logout_view


urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register'),
    path('forgot/',views.forgot, name='forgot'),
    
    #path('', views.home, name='home'),
    #path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]
