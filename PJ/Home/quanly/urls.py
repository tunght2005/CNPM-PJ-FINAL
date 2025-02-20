from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'quanly'  # Định nghĩa namespace
urlpatterns = [
    # Dashboard
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    
    # Employees
    path('employees/', views.employee_management, name='employee_management'),
    path('employees/add/', views.add_employee, name='add_employee'),
    
    # Products
    path('products/', views.product_management, name='product_management'),
    path('products/add/', views.add_product, name='add_product'),
    
    # Orders
    path('orders/', views.order_management, name='order_management'),
    path('orders/add/', views.add_order, name='add_order'),
    
    # Customers
    path('customers/', views.customer_management, name='customer_management'),
    path('customers/add/', views.add_customer, name='add_customer'),

    path('warranties/', views.warranty_management, name='warranty_management'),
    path('warranties/add/', views.add_warranty, name='add_warranty'),

    path('orders/', views.order_management, name='order_management'),
    path('orders/add/', views.add_order, name='add_order'),


]  
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)