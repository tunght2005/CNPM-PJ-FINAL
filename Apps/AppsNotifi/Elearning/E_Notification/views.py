# from django.shortcuts import render
# from django.http import HttpResponse

# def Notification(request):
#     notifications = Notification.objects.all() 
#     return render(request, 'home/notifi.html')

# from django.conf import settings
# from django.shortcuts import render
# from .models import Notification

# def notification_list(request):
#     notifications = Notification.objects.all() 
#     return render(request, 'home/notifi.html', {'notifications': notifications, 'MEDIA_URL': settings.MEDIA_URL}) 

from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Notification

def notification_list(request):
    notifications = Notification.objects.all()
    return render(request, 'home/notifi.html', {'notifications': notifications, 'MEDIA_URL': settings.MEDIA_URL})

@csrf_exempt
def mark_as_read(request, notification_id):
    """API: Đánh dấu thông báo là đã đọc"""
    if request.method == "POST":
        notification = get_object_or_404(Notification, id=notification_id)
        notification.is_read = True
        notification.save()
        return JsonResponse({"success": True, "is_read": notification.is_read})
    return JsonResponse({"success": False, "error": "Phương thức không hợp lệ"})

@csrf_exempt
def delete_notification(request, notification_id):
    """ Xóa thông báo khỏi database """
    if request.method == "DELETE":
        try:
            notification = get_object_or_404(Notification, id=notification_id)
            notification.delete()
            return JsonResponse({"success": True})
        except Notification.DoesNotExist:
            return JsonResponse({"success": False, "error": "Không tìm thấy thông báo."})
