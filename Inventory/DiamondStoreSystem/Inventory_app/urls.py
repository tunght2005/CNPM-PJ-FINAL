from django.urls import path
from Inventory_app import views

app_name = 'Inventory_app'
urlpatterns = [
    path('', views.home, name='home'),  # Trang chính
    path('inventory/', views.inventory_list, name='inventory_list'),
    path('add/', views.add_inventory, name='add_inventory'),
    path('transaction/', views.transaction_list, name='transaction_list'),
    path('add/', views.add_product, name='add_product'),
    path('list/', views.product_list, name='product_list'),
]
