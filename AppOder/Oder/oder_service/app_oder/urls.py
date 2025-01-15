from django.contrib import admin 
from django.urls import include, path
from . import views

urlpatterns = [
    path('form_add_don_hang/', views.form_add_don_hang, name='form_add_don_hang'),
    path('', views.table_data_oder, name='table_data_oder'),
    path('delete_order/<int:order_id>/', views.delete_order, name='delete_order'),
    path('edit_order/<int:order_id>/', views.edit_order, name='edit_order'),
]
