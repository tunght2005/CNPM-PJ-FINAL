from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps
from django.http import HttpResponseForbidden

def role_required(allowed_roles=[]):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.session.get('UserID'):
                messages.error(request, 'Vui lòng đăng nhập để tiếp tục')
                return redirect('login')
            
            user_role = request.session.get('user_role')
            if user_role in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden("Bạn không có quyền truy cập trang này!")
        return wrapper
    return decorator