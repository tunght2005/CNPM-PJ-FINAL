from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.decorators import role_required
from .models import User
from pj_home.models import *
from .forms import AddProductForm
from .forms import AddEmployeeForm
from .forms import AddCustomerForm
from .forms import AddEmployeeForm


#ADMIN
# Admin Dashboard
@role_required([6])  # Chỉ Admin
def admin_dashboard(request):
    print(f"Debug - Accessing admin dashboard with session: {request.session.items()}")
    try:
        return render(request, 'Admin/admin.html')
    except Exception as e:
        print(f"Debug - Error rendering admin dashboard: {str(e)}")
        messages.error(request, f'Lỗi hiển thị trang quản trị: {str(e)}')
        return redirect('home_page')

# Quản lý nhân viên

#Api
@role_required([6, 5])  #Admin
def employee_management(request):
    employees = User.objects.filter(role__in=[2,3,4])  # Sales, Staff, Delivery
    user_role = request.session.get('user_role')
    
    if user_role == 6:  # Admin
        template = 'Admin/table-data-table.html'
    elif user_role == 5:  # Manager
        template = 'Manager/table-data-table.html'
    
    return render(request, template, {'employees': employees})

@role_required([6, 5])  # Chỉ admin mới có quyền thêm nhân viên
def add_employee(request):
    user_role = request.session.get('user_role')
    
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            try:
                employee = form.save()
                messages.success(request, f'Thêm nhân viên {employee.username} thành công!')
                return redirect('quanly:employee_management')
            except Exception as e:
                messages.error(request, f'Lỗi khi thêm nhân viên: {str(e)}')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'Lỗi ở trường {field}: {error}')
    else:
        form = AddEmployeeForm()

    # Select template based on user role
    if user_role == 6:  # Admin
        template = 'Admin/form-add-nhan-vien.html'
    elif user_role == 5:  # Manager
        template = 'Manager/form-add-nhan-vien.html'
    
    return render(request, template, {'form': form})

# Quản lý sản phẩm
@role_required([6, 5])
def product_management(request):
    products = Product.objects.all()
    user_role = request.session.get('user_role')
    
    if user_role == 6:  # Admin
        template = 'Admin/table-data-product.html'
    elif user_role == 5:  # Manager
        template = 'Manager/table-data-product.html'
    
    return render(request, template, {'products': products})

@role_required([6, 5]) 
def add_product(request):
    user_role = request.session.get('user_role')
    
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                product = form.save()
                messages.success(request, f'Thêm sản phẩm {product.Pname} thành công!')
                return redirect('quanly:product_management')
            except Exception as e:
                messages.error(request, f'Lỗi khi thêm sản phẩm: {str(e)}')
    else:
        form = AddProductForm()

    # Select template based on user role
    if user_role == 6:  # Admin
        template = 'Admin/form-add-san-pham.html'
    elif user_role == 5:  # Manager
        template = 'Manager/form-add-san-pham.html'
    
    return render(request, template, {'form': form})

# Quản lý khách hàng

#Api
@role_required([5, 6])  # Manager và Admin   
def customer_management(request):
    customers = User.objects.filter(role=1)  # Role 1 là khách hàng
    user_role = request.session.get('user_role')
    
    if user_role == 6:  # Admin
        template = 'Admin/page-customer.html'
    elif user_role == 5:  # Manager
        template = 'Manager/page-customer.html'
    
    return render(request, template, {'customers': customers})

@role_required([5, 6])
def add_customer(request):
    user_role = request.session.get('user_role')
    
    if request.method == 'POST':
        form = AddCustomerForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                user = form.save()
                user.save()
                messages.success(request, 'Thêm khách hàng thành công!')
                return redirect('quanly:customer_management')
            except Exception as e:
                messages.error(request, f'Lỗi: {str(e)}')
    else:
        form = AddCustomerForm()

    # Chọn template dựa vào role
    if user_role == 6:  # Admin
        template = 'Admin/form-add-user.html'
    elif user_role == 5:  # Manager
        template = 'Manager/form-add-user.html'
    
    return render(request, template, {'form': form})

# Quản lý bảo hành
@role_required([6])  # Chỉ Admin
def warranty_management(request):
    warranties = Warranty.objects.all()
    return render(request, 'Admin/table-data-warranty.html', {'warranties': warranties})

@role_required([6])
def add_warranty(request):
    return render(request, 'Admin/form-add-warranty.html')

# Quản lý đơn hàng
@role_required([6, 5])  # Admin và Manager
def order_management(request):
    orders = Order.objects.all()
    user_role = request.session.get('user_role')
    
    if user_role == 6:  # Admin
        template = 'Admin/table-data-oder.html'
    elif user_role == 5:  # Manager 
        template = 'Manager/table-data-oder.html'
    
    return render(request, template, {'orders': orders})

@role_required([6, 5])
def add_order(request):
    user_role = request.session.get('user_role')
    
    # Select template based on user role
    if user_role == 6:  # Admin
        template = 'Admin/form-add-order.html'
    elif user_role == 5:  # Manager
        template = 'Manager/form-add-order.html'
    
    return render(request, template)

@role_required([6])
def add_gift(request):
    return render(request, 'Admin/form-add-uudai.html')

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


#MANAGER
@role_required([5])  # Chỉ Manager
def manager_dashboard(request):
    return render(request, 'Manager/manager.html')

@role_required([5, 4]) 
def block(request):
    user_role = request.session.get('user_role') 
    
    # Select template based on user role
    if user_role == 5:  # 
        template = 'Manager/Block.html'
    elif user_role == 5:  # Manager
        template = 'DeliveryStaff/Block.html'
    
    return render(request, template)

#DELIVERY_STAFF
@role_required([4])  # Chỉ Delivery Staff
def delivery_staff_dashboard(request):
    return render(request, 'DeliveryStaff/deliveryStaff.html')
