from django import forms  # Thêm dòng này để import forms 
from django.contrib import admin 
from .models import Customer, Product, Order, OrderItem

# Tùy chỉnh OrderItemForm
class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'quantity', 'price']
    
    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['price'] = cleaned_data['product'].price  # Tự động lấy giá của sản phẩm
        return cleaned_data

# Tùy chỉnh Admin
class OrderItemAdmin(admin.ModelAdmin):
    form = OrderItemForm

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status', 'total_amount', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('customer__first_name', 'customer__last_name')

    def mark_as_shipped(modeladmin, request, queryset):
        queryset.update(status=Order.SHIPPED)
    mark_as_shipped.short_description = "Mark selected orders as shipped"

    actions = [mark_as_shipped]

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    search_fields = ('name',)

admin.site.register(Customer)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)

