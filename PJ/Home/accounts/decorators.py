from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps

def role_required(allowed_roles=[]):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper_func(request, *args, **kwargs):
            print(f"Debug - Current session: {request.session.items()}")
            print(f"Debug - Required roles: {allowed_roles}")
            
            # Kiểm tra xem user đã đăng nhập chưa
            if 'user_id' not in request.session:
                messages.error(request, 'Vui lòng đăng nhập để tiếp tục')
                return redirect('login')
            
            # Lấy role từ session
            user_role = request.session.get('user_role')
            print(f"Debug - User role from session: {user_role}")
            
            if user_role in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                messages.error(request, 'Bạn không có quyền truy cập trang này')
                return redirect('home_page')
                
        return wrapper_func
    return decorator