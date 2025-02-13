from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.decorators import role_required
from accounts.models import User
from .models import *
from .forms import AddProductForm

#ADMIN
# Admin Dashboard
@role_required([6])  # Chỉ Admin
def admin_dashboard(request):
    return render(request, 'Admin/admin.html')

# Quản lý nhân viên
@role_required([6])  #Admin
def employee_management(request):
    employees = User.objects.filter(role__in=[2,3,4])  # Sales, Staff, Delivery
    return render(request, 'Admin/table-data-table.html', {'employees': employees})

@role_required([6])
def add_employee(request):
    return render(request, 'Admin/form-add-nhan-vien.html')

# Quản lý sản phẩm
@role_required([6])
def product_management(request):
    products = Product.objects.all()
    return render(request, 'Admin/table-data-product.html', {'products': products})

@role_required([6])
def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Thêm sản phẩm thành công!')
            return redirect('quanly:product_management')
        else:
            messages.error(request, 'Vui lòng kiểm tra lại thông tin!')
    else:
        form = AddProductForm()
    
    return render(request, 'Admin/form-add-san-pham.html', {'form': form})

# Quản lý đơn hàng
@role_required([6])  # Sales trở lên
def order_management(request):
    orders = Order.objects.all()
    return render(request, 'Admin/table-data-oder.html', {'orders': orders})

# Quản lý khách hàng
@role_required([5, 6])  # Manager và Admin
def customer_management(request):
    customers = User.objects.filter(role=1)  # Role 1 là khách hàng
    return render(request, 'Admin/page-customer.html', {'form': customers})

@role_required([5, 6])
def add_customer(request):
    return render(request, 'Sdmin/form-add-user.html')

# Quản lý bảo hành
@role_required([6])  # Chỉ Admin
def warranty_management(request):
    warranties = Warranty.objects.all()
    return render(request, 'Admin/table-data-warranty.html', {'warranties': warranties})

@role_required([6])
def add_warranty(request):
    return render(request, 'Admin/form-add-warranty.html')

# Quản lý đơn hàng
@role_required([6])  # Chỉ Admin
def order_management(request):
    orders = Order.objects.all()
    return render(request, 'Admin/table-data-oder.html', {'orders': orders})

@role_required([6])
def add_order(request):
    return render(request, 'Admin/form-add-order.html')

#

# Quản lý tin tức
# @role_required([3, 5, 6])  # Staff, Manager, Admin
# def news_management(request):
#     news = News.objects.all()
#     return render(request, 'quanly/admin/table-data-info.html', {'news': news})

# Form thêm tin tức
# @role_required([3, 5, 6])
# def add_news(request):
#     if request.method == 'POST':
#         # Xử lý thêm tin tức
#         pass
#     return render(request, 'quanly/admin/form-add-news.html')
