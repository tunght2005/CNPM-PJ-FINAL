from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import User
from django.contrib import messages
from .decorators import role_required
import bcrypt
from django.contrib.auth.hashers import check_password  # Thêm import này

def register(request):
    #if request.session.get('user_id'):
    #    return redirect('home')
        
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            user.is_active = True
            user.role = 1  # Set default role as Customer
            user.save()
            messages.success(request, 'Đăng ký thành công! Vui lòng đăng nhập.')
            return redirect('login')    
    return render(request, 'register.html', {'form': form})

def login(request):
    #if request.session.get('user_id'):
    #    return redirect('home')
        
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if not email or not password:
            messages.error(request, 'Vui lòng nhập đầy đủ email và mật khẩu')
            return render(request, 'login.html')

        try:
            user = User.objects.get(email=email)
            if not user.is_active:
                messages.error(request, 'Tài khoản chưa được kích hoạt')
                return render(request, 'login.html')
            
            # Kiểm tra cả 2 loại mật khẩu
            password_valid = False
            try:
                # Thử kiểm tra với bcrypt
                password_valid = bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8'))
            except ValueError:
                # Nếu không phải bcrypt, kiểm tra với Django's password hasher
                password_valid = check_password(password, user.password)
                
            if password_valid:
                # Lưu thông tin user vào session
                request.session['user_id'] = user.userid
                request.session['user_email'] = user.email
                request.session['user_name'] = user.username
                request.session['user_role'] = user.role
                
                messages.success(request, f'Chào mừng {user.username}!')
                
                # Điều hướng dựa trên role
                if user.role == 6:  #Admin
                    # return redirect('admin_dashboard')
                    return redirect('quanly:admin_dashboard')
                elif user.role == 5:  # Manager
                    return redirect('manager_dashboard')
                elif user.role == 4:  # Delivery Staff
                    return redirect('delivery_dashboard')
                elif user.role == 3:  
                    return redirect('salestaff_dashboard')
                elif user.role in [3]:  # Sales và Staff
                    return redirect('staff_dashboard')
                else:  # Customer và Guest
                    return redirect('home')
            else:
                messages.error(request, 'Email hoặc mật khẩu không đúng')
        except User.DoesNotExist:
            messages.error(request, 'Email hoặc mật khẩu không đúng')
            
    return render(request, 'login.html')

def logout(request):
    request.session.flush()
    messages.success(request, 'Đăng xuất thành công!')
    return redirect('login')

def forgot(request):
    if request.session.get('user_id'):
        return redirect('home')
        
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            messages.success(request, 'Vui lòng liên hệ admin để đặt lại mật khẩu')
        except User.DoesNotExist:
            messages.error(request, 'Email không tồn tại trong hệ thống')
    return render(request, 'forgot.html')

# Admin Views
# @role_required([5, 6])
# def admin_dashboard(request):
#     return render(request, 'admin/dashboard.html')

# @role_required([5, 6])
# def manage_users(request):
#     users = User.objects.all()
#     return render(request, 'admin/users.html', {'users': users})

# # Staff Views
# @role_required([2, 3, 4, 5, 6])
# def staff_dashboard(request):
#     return render(request, 'staff/dashboard.html')

# # Delivery Staff Views
# @role_required([4])
# def delivery_dashboard(request):
#     return render(request, 'delivery/dashboard.html')

# # Customer Views
# @role_required([1, 2, 3, 4, 5, 6])
# def profile(request):
#     user = User.objects.get(userid=request.session['user_id'])
#     return render(request, 'profile.html', {'user': user})

@role_required([1, 2, 3, 4, 5, 6])
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        user = User.objects.get(userid=request.session['user_id'])
        
        if not bcrypt.checkpw(old_password.encode('utf-8'), user.password.encode('utf-8')):
            messages.error(request, 'Mật khẩu cũ không đúng')
        elif new_password != confirm_password:
            messages.error(request, 'Mật khẩu mới không khớp')
        else:
            user.password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            user.save()
            messages.success(request, 'Đổi mật khẩu thành công')
            return redirect('profile')
            
    return render(request, 'change_password.html')