from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.decorators import role_required
from .models import User
from pj_home.models import *
from .forms import AddProductForm
from .forms import AddEmployeeForm

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
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # Tạo user mới
                user = form.save(commit=False)
                # Set mật khẩu mặc định (có thể là số điện thoại)
                user.set_password(form.cleaned_data['phone'])
                user.save()
                
                messages.success(request, 'Thêm nhân viên thành công!')
                return redirect('quanly:employee_management')
            except Exception as e:
                messages.error(request, f'Lỗi: {str(e)}')
    else:
        form = AddEmployeeForm()
    
    return render(request, 'Admin/form-add-nhan-vien.html', {'form': form})

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
            # Lấy dữ liệu từ form
            product = form.save(commit=False)
            
            # Tính toán giá
            diamond_cost = float(request.POST.get('diamondCost', 0))
            labor_cost = float(request.POST.get('laborCost', 0))
            diamond_shell_cost = float(request.POST.get('diamondShellCost', 0))
            
            # Tính giá vốn
            cost_price = diamond_cost + labor_cost + diamond_shell_cost
            
            # Tính giá bán dựa trên tỉ lệ áp giá
            price_ratio = float(request.POST.get('priceRatio', 0))
            selling_price = cost_price * (1 + price_ratio/100)
            
            # Cập nhật giá bán vào sản phẩm
            product.price = selling_price
            product.save()
            
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

@role_required([6])
def add_employee(request):
    return render(request, 'Admin/form-add-nhan-vien.html')

# Quản lý khách hàng
@role_required([5, 6])  # Manager và Admin
def customer_management(request):
    customers = User.objects.filter(role=1)  # Role 1 là khách hàng
    return render(request, 'Admin/page-customer.html', {'form': customers})

@role_required([5, 6])
def add_customer(request):
    return render(request, 'Admin/form-add-user.html')

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
