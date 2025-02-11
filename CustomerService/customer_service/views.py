from django.shortcuts import render
from .models import Customer, Promotion

# Hiển thị danh sách khách hàng
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer.html', {'customers': customers})

# Hiển thị danh sách chương trình khuyến mãi
def promotion_list(request):
    promotions = Promotion.objects.all()
    return render(request, 'gift.html', {'promotions': promotions})
