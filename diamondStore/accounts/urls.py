from django.urls import path
from .views import login_out
from .views import forgot

urlpatterns = [
    path('login-out/',login_out , name='login_out'),
    path('forgot/',forgot, name='forgot'),
]
