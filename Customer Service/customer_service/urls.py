from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.customer_list, name='customer_list'),
    path('promotions/', views.promotion_list, name='promotion_list'),
]
