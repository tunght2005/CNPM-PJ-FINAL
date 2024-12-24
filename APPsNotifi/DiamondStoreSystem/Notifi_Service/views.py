from rest_framework import viewsets
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def create(self, request, *args, **kwargs):
        # Nhận dữ liệu và tạo thông báo
        data = request.data
        notification = Notification.objects.create(
            title=data['title'],
            message=data['message'],
            customer_email=data['customer_email']
        )
        notification.save()
        return Response({"message": "Notification sent successfully!"})

# Form có sẳn
# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Notification

# def notification_list(request):
#     notifications = Notification.objects.all()
#     return render(request, 'notification.html', {'notifications': notifications})

# def mark_as_read(request, notification_id):
#     notification = get_object_or_404(Notification, id=notification_id)
#     if request.method == 'POST':
#         notification.is_read = True
#         notification.save()
#         return redirect('notifi-list')  # Đảm bảo tên URL là chính xác
#     return redirect('notifi-list')  # Nếu không phải POST, cũng chuyển hướng

# def delete_notification(request, notification_id):
#     notification = get_object_or_404(Notification, id=notification_id)
#     if request.method == 'POST':
#         notification.delete()
#         return redirect('notifi-list')  # Sửa lỗi dấu ngoặc kép
#     return redirect('notifi-list')  # Nếu không phải POST, cũng chuyển hướng


