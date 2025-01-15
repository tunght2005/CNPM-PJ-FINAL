from django import forms
from .models import Order, Customer, Product, OrderItem

class OrderForm(forms.Form):
    customer_name = forms.CharField(
        label='Tên khách hàng', 
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    customer_phone = forms.CharField(
        label='Số điện thoại khách hàng', 
        max_length=15, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    customer_address = forms.CharField(
        label='Địa chỉ khách hàng', 
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    seller_name = forms.CharField(
        label='Tên người bán', 
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    seller_id = forms.CharField(
        label='Số điện thoại người bán', 
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    order_date = forms.DateField(
        label='Ngày làm đơn hàng', 
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    product_name = forms.CharField(
        label='Tên sản phẩm cần bán', 
        max_length=200, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    product_code = forms.CharField(
        label='Mã sản phẩm', 
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    quantity = forms.IntegerField(
        label='Số lượng', 
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    status = forms.ChoiceField(
        label='Tình trạng', 
        choices=[
            ('Đã xử lý', 'Đã xử lý'),
            ('Đang chờ', 'Đang chờ'),
            ('Đã hủy', 'Đã hủy'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    note = forms.CharField(
        label='Ghi chú đơn hàng', 
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}), 
        required=False
    )