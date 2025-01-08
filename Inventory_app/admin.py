from django.contrib import admin
from .models import Product, Supplier, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'status', 'category', 'supplier']

    def name (self, obj):
        return obj.name
    
    def price(self, obj):
        return obj.price
    # Nếu các trường không có trong mô hình nhưng bạn muốn hiển thị một giá trị tùy chỉnh:
    def status(self, obj):
        return obj.status

    def category(self, obj):
        return obj.category.name  # Nếu category là một đối tượng liên kết và bạn muốn hiển thị tên

    def supplier(self, obj):
        return obj.supplier.name  # Tương tự với supplier

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Category, CategoryAdmin)
