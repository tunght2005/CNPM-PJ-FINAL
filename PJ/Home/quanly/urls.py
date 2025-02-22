from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'quanly'  # Định nghĩa namespace
urlpatterns = [
    #ADMIN
    # Dashboard
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    
    # Employees
    path('employees/', views.employee_management, name='employee_management'),
    path('employees/add/', views.add_employee, name='add_employee'),
    path('delete-employee/<str:user_id>/', views.delete_employee, name='delete_employee'),
    
    # Products
    path('products/', views.product_management, name='product_management'),
    path('products/add/', views.add_product, name='add_product'),
    path('delete-product/<str:product_id>/', views.delete_product, name='delete_product'),

    # Orders
    path('orders/', views.order_management, name='order_management'),
    path('orders/add/', views.add_order, name='add_order'),
    path('order/delete/<str:order_id>/', views.delete_order, name='delete_order'),
    path('order/update-status/<str:order_id>/', views.update_order_status, name='update_order_status'),
    # Customers
    path('customers/', views.customer_management, name='customer_management'),
    path('customers/add/', views.add_customer, name='add_customer'),
    path('delete-customer/<str:user_id>/', views.delete_customer, name='delete_customer'),

    path('warranties/', views.warranty_management, name='warranty_management'),
    path('warranties/add/', views.add_warranty, name='add_warranty'),

    path('orders/', views.order_management, name='order_management'),
    path('orders/add/', views.add_order, name='add_order'),

    #banned
    path('ban_management/', views.ban_management, name='ban_management'),
    path('ban', views.ban, name='ban'),

    #money
    path('money_management/', views.money_management, name='money_management'),
    path('money', views.money, name='money'),




    #MANAGER
    path('manager_dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('blocked/', views.block, name='block'),

    #DELIVERY_STAFF
    path('delivery_staff_dashboard/', views.delivery_staff_dashboard, name='delivery_staff_dashboard'),
    path('delivery', views.delivery_management, name='delivery_manangement'),

    
]  
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)