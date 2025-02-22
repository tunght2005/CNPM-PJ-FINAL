from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import User
from django.contrib import messages
from .decorators import role_required
from django.contrib.auth import logout
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required
import bcrypt
from django.urls import reverse
from django.contrib.auth.hashers import check_password  # Thêm import này

from django.http import JsonResponse


def register(request):
    if request.session.get('user_id'):
        return redirect('home_page')
        
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            user.is_active = True
            user.role = 2  # Set default role as Customer
            user.save()
            messages.success(request, 'Đăng ký thành công! Vui lòng đăng nhập.')
            return redirect('login')    
    return render(request, 'register.html', {'form': form})

def login(request):
    # if request.session.get('user_id'):
    #     return redirect('home_page1')
    #     #return redirect('quanly:admin_dashboard')

    if request.session.get('user_id'):
        user_role = request.session.get('user_role')
        if user_role == 6:
            return redirect('quanly:admin_dashboard')
        return redirect('home_page1')

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
                # Đảm bảo session lưu đúng key
                request.session['user_id'] = str(user.UserID)  # Chuyển thành chuỗi để tránh lỗi
                request.session['user_email'] = user.email
                request.session['user_name'] = user.username
                request.session['user_role'] = int(user.role)  # Đảm bảo role là số nguyên
                
                # Thêm debug print
                print(f"User Role: {request.session['user_role']}")
                print(f"Redirecting user with role {user.role}")
                # Debug session
                print("Đăng nhập thành công! Session lưu:", request.session.items())

                messages.success(request, f'Chào mừng {user.username}!')
                
                
                # Điều hướng theo role
                if int(user.role) == 6:  #Admin
                    # return redirect('admin_dashboard')
                   print("Debug - Redirecting admin to dashboard")
                   return redirect('quanly:admin_dashboard')
                elif int(user.role) == 5:  # Manager
                    return redirect('quanly:manager_dashboard') 
                elif int(user.role) == 4:  # Delivery Staff
                    return redirect('quanly:delivery_staff_dashboard')
                elif int(user.role) == 3:  # Sales và Staff
                    return redirect('quanly:sale_dashboard')
                elif int(user.role) == 2:  # Customer
                    return redirect('home_page1')
                else:  #Guest (no login)
                    return redirect('home_page')

            else:
                messages.error(request, 'Email hoặc mật khẩu không đúng')
        except User.DoesNotExist:
            messages.error(request, 'Email hoặc mật khẩu không đúng')

    return render(request, 'login.html')

def logout_view(request):
    request.session.flush()  # Xóa toàn bộ session
    messages.success(request, 'Đăng xuất thành công!')
    return redirect('home_page')

def forgot(request):
    if request.session.get('user_id'):
        return redirect('home_page1')
        
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            messages.success(request, 'Vui lòng liên hệ admin để đặt lại mật khẩu')
        except User.DoesNotExist:
            messages.error(request, 'Email không tồn tại trong hệ thống')
    return render(request, 'forgot.html')


@role_required([1, 2, 3, 4, 5, 6])
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        user = User.objects.get(UserID=request.session['user_id'])
        
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

