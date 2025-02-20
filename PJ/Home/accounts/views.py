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

from django.http import JsonResponse


def register(request):
    if request.session.get('user_id'):
        return redirect('home')
        
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

# def login(request):
#     if request.session.get('user_id'):
#         return redirect('home_page1')
        
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
        
#         if not email or not password:
#             messages.error(request, 'Vui lòng nhập đầy đủ email và mật khẩu')
#             return render(request, 'login.html')

#         try:
#             user = User.objects.get(email=email)
#             if not user.is_active:
#                 messages.error(request, 'Tài khoản chưa được kích hoạt')
#                 return render(request, 'login.html')
                
#             if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
#                 # Lưu thông tin user vào session
#                 request.session['user_id'] = user.UserID
#                 request.session['user_email'] = user.email
#                 request.session['user_name'] = user.username
#                 request.session['user_role'] = user.role
#                 # Kiểm tra session sau khi đăng nhập
#                 print("Session user_id:", request.session.get('user_id'))
#                 print("Session user_email:", request.session.get('user_email'))
#                 print("Session user_name:", request.session.get('user_name'))
#                 print("Session user_role:", request.session.get('user_role'))
#                 messages.success(request, f'Chào mừng {user.username}!')
                
#                 # Điều hướng dựa trên role
#                 if int(user.role) >= 5:  # Manager và Admin
#                     return redirect('admin_dashboard')
#                 elif int(user.role) == 4:  # Delivery Staff
#                     return redirect('delivery_dashboard')
#                 elif int(user.role) in [2, 3]:  # Sales và Staff
#                     return redirect('staff_dashboard')
#                 else:  # Customer và Guest
#                     return redirect('customer_page')
#             else:
#                 messages.error(request, 'Email hoặc mật khẩu không đúng')
#         except User.DoesNotExist:
#             messages.error(request, 'Email hoặc mật khẩu không đúng')
            
#     return render(request, 'login.html')
def login(request):
    if request.session.get('user_id'):
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

            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                # Đảm bảo session lưu đúng key
                request.session['user_id'] = str(user.UserID)  # Chuyển thành chuỗi để tránh lỗi
                request.session['user_email'] = user.email
                request.session['user_name'] = user.username
                request.session['user_role'] = int(user.role)  # Đảm bảo role là số nguyên

                # Debug session
                print("Đăng nhập thành công! Session lưu:", request.session.items())

                messages.success(request, f'Chào mừng {user.username}!')
                
                # Điều hướng theo role
                if int(user.role) == 6:  #Admin
                    # return redirect('admin_dashboard')
                   return redirect('quanly:admin_dashboard')
                elif int(user.role) == 5:  # Manager
                    return redirect('manager_dashboard')
                elif int(user.role) == 4:  # Delivery Staff
                    return redirect('delivery_dashboard')
                elif int(user.role) == 3:  # Sales và Staff
                    return redirect('staff_dashboard')
                elif int(user.role) == 2:
                    return redirect('home_page1') 
                else:  #Guest
                    return redirect('home_page')

            else:
                messages.error(request, 'Email hoặc mật khẩu không đúng')
        except User.DoesNotExist:
            messages.error(request, 'Email hoặc mật khẩu không đúng')

    return render(request, 'login.html')

# def logout(request):
#     request.session.flush()
#     messages.success(request, 'Đăng xuất thành công!')
#     return redirect('login')
# def logout_view(request):
#     logout(request)
    
#     # Xóa từng key trong session
#     keys_to_delete = ['UserID', 'email', 'username', 'role']
#     for key in keys_to_delete:
#         if key in request.session:
#             del request.session[key]
    
#     request.session.flush()  # Xóa hoàn toàn session
#     request.session.clear()
    
#     messages.success(request, 'Đăng xuất thành công!')
#     return redirect('home_page')
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

# Admin Views
@role_required([5, 6])
def admin_dashboard(request):
    return render(request, 'Admin/dashboard.html')

@role_required([5, 6])
def manage_users(request):
    users = User.objects.all()
    return render(request, 'Admin/users.html', {'users': users})

# Staff Views
@role_required([2, 3, 4, 5, 6])
def staff_dashboard(request):
    return render(request, 'staff/dashboard.html')

# Delivery Staff Views
@role_required([4])
def delivery_dashboard(request):
    return render(request, 'delivery/dashboard.html')

# Customer Views
@role_required([1, 2, 3, 4, 5, 6])
def profile(request):
    user = User.objects.get(UserID=request.session['user_id'])
    return render(request, 'profile.html', {'user': user})

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


# from django.shortcuts import render, redirect
# from .forms import RegistrationForm
# from .models import Users
# from django.contrib import messages
# import bcrypt

# def register(request):
#     form = RegistrationForm()
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=True)
#             user.is_active = True  # Set user as active immediately
#             user.save()
#             messages.success(request, 'Registration successful! Please login.')
#             return redirect('login')    
#     return render(request, 'register.html', {'form': form})

# def login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
        
#         if not email or not password:
#             messages.error(request, 'Vui lòng nhập đầy đủ email và mật khẩu')
#             return render(request, 'login.html')

#         try:
#             user = Users.objects.get(email=email)
#             if not user.is_active:
#                 messages.error(request, 'Tài khoản chưa được kích hoạt')
#                 return render(request, 'login.html')
                
#             if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
#                 # Lưu thông tin user vào session
#                 request.session['user_id'] = user.userid
#                 request.session['user_email'] = user.email
#                 request.session['user_name'] = user.username
                
#                 messages.success(request, f'Chào mừng {user.username}!')
#                 return redirect('home')
#             else:
#                 messages.error(request, 'Email hoặc mật khẩu không đúng')
#         except Users.DoesNotExist:
#             messages.error(request, 'Email hoặc mật khẩu không đúng')
            
#     return render(request, 'login.html')

# def forgot(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         try:
#             user = Users.objects.get(email=email)
#             # Add alternative password reset logic here if needed
#             messages.success(request, 'Please contact administrator for password reset')
#         except Users.DoesNotExist:
#             messages.error(request, 'Email not found')
#     return render(request, 'forgot.html')






# from django.shortcuts import render, redirect
# from .forms import RegistrationForm
# from .models import Users
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes, force_str
# from django.template.loader import render_to_string
# from django.contrib.sites.shortcuts import get_current_site
# from .token import account_activation_token
# from django.contrib import messages
# from django.core.mail import EmailMessage
# from django.urls import reverse

# def register(request):
#     form = RegistrationForm()
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=True)
#             user.is_active = False
#             user.save()

#             current_site = get_current_site(request)
#             mail_subject = 'Activate your account'
#             message = render_to_string('account_activation_email.html', {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(user.userid)),
#                 'token': account_activation_token.make_token(user)
#             })
            
#             to_email = form.cleaned_data.get('email')
#             email = EmailMessage(
#                 mail_subject, message, to=[to_email]
#             )
#             email.send()
#             messages.success(request, 'Please check your email to complete registration')
#             return redirect('welcome')    
#     return render(request, 'register.html', {'form': form})

# def activate(request, uidb64, token):
#     try:
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         user = Users.objects.get(userid=uid)
#     except (TypeError, ValueError, OverflowError, Users.DoesNotExist):
#         user = None

#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         messages.success(request, 'Account activated successfully')
#         return redirect('login')
#     else:
#         messages.error(request, 'Invalid activation link')
#         return redirect('welcome')

# import bcrypt

# def login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         try:
#             user = Users.objects.get(email=email)
#             if user is not None and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
#                 messages.success(request, 'Login successful')
#                 return redirect('home')
#             else:
#                 messages.error(request, 'Invalid credentials')
#         except Users.DoesNotExist:
#             messages.error(request, 'Invalid credentials')
#     return render(request, 'login.html')

# def forgot(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         try:
#             user = Users.objects.get(email=email)
#             # Add password reset logic here
#             messages.success(request, 'Password reset instructions sent to your email')
#         except Users.DoesNotExist:
#             messages.error(request, 'Email not found')
#     return render(request, 'forgot.html')

# # def home(request):
# #     return render(request, 'home.html')