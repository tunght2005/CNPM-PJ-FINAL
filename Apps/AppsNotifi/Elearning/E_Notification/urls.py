# from django.urls import path
# from . import views

# urlpatterns = [
#     # path('E_Notification/', views.Notification, name='E_Notification'),
#     path('', views.Notification, name='E_Notification'),
# ]
# from django.urls import path
# from .views import notification_list
# from django.conf import settings
# from django.conf.urls.static import static
# urlpatterns = [
#     path('', notification_list, name='notifications'),  
# ]

# # Chỉ sử dụng khi chạy server local (development mode)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from .views import notification_list, mark_as_read, delete_notification
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', notification_list, name='notifications'),  
    path('mark-as-read/<int:notification_id>/', mark_as_read, name='mark_as_read'),
    path('delete-notification/<int:notification_id>/', delete_notification, name='delete_notification'),
]

# Chỉ sử dụng khi chạy server local (development mode)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
