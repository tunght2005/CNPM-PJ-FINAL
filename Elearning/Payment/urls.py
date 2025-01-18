from django.urls import path 
from . import views

urlpatterns = [
    path('',views.Payment,name='Payment'),
    path('manage_order/', views.manage_order,name='manage_order')
]
