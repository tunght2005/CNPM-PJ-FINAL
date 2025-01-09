from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('',views.Payment,name='Payment'),
    path('Payment/', views.user, name='Payment'),
    path('Payment/', views.PaymentMethod, name='Payment'),
    path('Payment/', views.TransactionHistory, name='Payment'),
    path('Payment/', views.Notification, name='Payment'),
]