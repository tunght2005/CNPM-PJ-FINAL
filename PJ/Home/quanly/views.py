from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.decorators import role_required
from .models import User
from .models import Product
from pj_home.models import *
from .forms import AddProductForm
from .forms import AddEmployeeForm
from .forms import AddCustomerForm
from .forms import AddEmployeeForm
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.views.decorators.http import require_POST
#from .forms import AddOrderForm


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
    # Lấy nhân viên có role là 3 (SaleStaff) và 4 (Delivery Staff)
    employees = User.objects.filter(role__in=[3, 4]).select_related('employee')
    user_role = request.session.get('user_role')
    
    context = {
        'employees': employees
    }
    
    if user_role == 6:  # Admin
        template = 'Admin/table-data-table.html'
    elif user_role == 5:  # Manager
        template = 'Manager/table-data-table.html'
    
    return render(request, template, context)

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
    
    context = {
        'products': products
    }

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
    customers = User.objects.filter(role=2)  # Role 2 là khách hàng
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

@require_POST
@role_required([5, 6])  # Chỉ Manager và Admin có quyền xóa
def delete_customer(request, user_id):
    try:
        # Lấy user với role=2 (customer) và UserID tương ứng
        customer = User.objects.get(UserID=user_id, role=2)
        username = customer.username  # Lưu tên trước khi xóa
        
        # Xóa user và các bản ghi liên quan
        customer.delete()
        
        return JsonResponse({
            'status': 'success',
            'message': f'Đã xóa khách hàng {username} thành công'
        })
    except User.DoesNotExist:
        return JsonResponse({
            'status': 'error',
            'message': 'Không tìm thấy khách hàng'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)
    
@require_POST
@role_required([5, 6])  # Chỉ Manager và Admin có quyền xóa
def delete_employee(request, user_id):
    try:
        # Lấy user với role là 3 (SaleStaff) hoặc 4 (DeliveryStaff)
        employee = User.objects.get(UserID=user_id, role__in=[3, 4])
        username = employee.username  # Lưu tên trước khi xóa
        
        # Xóa user và các bản ghi liên quan
        employee.delete()
        
        return JsonResponse({
            'status': 'success',
            'message': f'Đã xóa nhân viên {username} thành công'
        })
    except User.DoesNotExist:
        return JsonResponse({
            'status': 'error',
            'message': 'Không tìm thấy nhân viên'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)

@require_POST
@role_required([5, 6])  # Chỉ Manager và Admin có quyền xóa
def delete_product(request, product_id):
    try:
        product = Product.objects.get(ProductID=product_id)
        product_name = product.Pname  # Lưu tên sản phẩm trước khi xóa
        
        # Xóa sản phẩm và các bản ghi liên quan
        product.delete()
        
        return JsonResponse({
            'status': 'success',
            'message': f'Đã xóa sản phẩm {product_name} thành công'
        })
    except Product.DoesNotExist:
        return JsonResponse({
            'status': 'error',
            'message': 'Không tìm thấy sản phẩm'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)

# Quản lý bảo hành
@role_required([6])  # Chỉ Admin
def warranty_management(request):
    warranties = Warranty.objects.all()
    return render(request, 'Admin/table-data-warranty.html', {'warranties': warranties})

@role_required([6])
def add_warranty(request):
    return render(request, 'Admin/form-add-warranty.html')

# Quản lý đơn hàng
@role_required([6, 5, 4])  # Admin và Manager và delivery staff
def order_management(request):
    orders = Order.objects.all()
    user_role = request.session.get('user_role')
    
    if user_role == 6:  # Admin
        template = 'Admin/table-data-oder.html'
    elif user_role == 5:  # Manager 
        template = 'Manager/table-data-oder.html'
    elif user_role == 4:  # Delivery Staff
        template = 'DeliveryStaff/table-data-oder.html'
    
    return render(request, template, {'orders': orders})

@role_required([6, 5, 4])
def add_order(request):
    user_role = request.session.get('user_role')
    
    if user_role == 6:  # Admin
        template = 'Admin/form-add-order.html'
    elif user_role == 5:  # Manager
        template = 'Manager/form-add-order.html'
    elif user_role == 4:  # Delivery Staff
        template = 'DeliveryStaff/form-add-order.html'
    
    return render(request, template) #, {'form': form}

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
    elif user_role == 4:  # Manager
        template = 'DeliveryStaff/Block.html'
    
    return render(request, template)

#DELIVERY_STAFF
@role_required([4])  # Chỉ Delivery Staff
def delivery_staff_dashboard(request):
    return render(request, 'DeliveryStaff/deliveryStaff.html')


@role_required([6, 5, 4])  # Admin và Manager và delivery staff
def delivery_management(request):
    #orders = Order.objects.all()
    user_role = request.session.get('user_role')
    
    if user_role == 6:  # Admin
        template = 'Admin/table-data-transport.html'
    elif user_role == 5:  # Manager 
        template = 'Manager/table-data-transport.html'
    elif user_role == 4:  # Delivery Staff
        template = 'DeliveryStaff/table-data-transport.html'
    
    return render(request, template)

@role_required([6])  # Admin 
def ban_management(request):
    return render(request, 'Admin/table-data-banned.html')

@role_required([6])  # Admin 
def ban(request):
    return render(request, 'Admin/form-add-bi-cam.html')

@role_required([6, 5])  # Admin va Manager
def money_management(request):
    user_role = request.session.get('user_role')
    if user_role == 6:  # Admin
        template = 'Admin/table-data-money.html'
    elif user_role == 5:  # Manager 
        template = 'Manager/table-data-money.html'
    return render(request, template)

@role_required([6,5])
def money(request):
    user_role = request.session.get('user_role')
    if user_role == 6:  # Admin
        template = 'Admin/form-add-tien-luong.html'
    elif user_role == 5:  # Manager 
        template = 'Manager/form-add-tien-luong.html'
    return render(request, template)

@role_required([6, 5, 4])  # Admin và Manager và delivery staff
def order_management(request):
    orders = Order.objects.all()
    user_role = request.session.get('user_role')
    
    if user_role == 6:  # Admin
        template = 'Admin/table-data-oder.html'
    elif user_role == 5:  # Manager 
        template = 'Manager/table-data-oder.html'
    elif user_role == 4:  # Delivery Staff
        template = 'DeliveryStaff/table-data-oder.html'
    
    return render(request, template, {'orders': orders})
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

@require_POST
def delete_order(request, order_id):
    try:
        order = get_object_or_404(Order, OrderID=order_id)
        order.delete()
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@require_POST
def update_order_status(request, order_id):
    try:
        order = get_object_or_404(Order, OrderID=order_id)
        new_status = request.POST.get('status')
        
        # Validate status
        valid_statuses = ['pending', 'shipping', 'delivered', 'cancelled']
        if new_status not in valid_statuses:
            return JsonResponse({
                'status': 'error',
                'message': 'Invalid status'
            }, status=400)
            
        order.status = new_status
        order.save()
        
        return JsonResponse({
            'status': 'success',
            'message': 'Status updated successfully'
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)