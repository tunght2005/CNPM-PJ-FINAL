"""
URL configuration for DiamondStoreSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
# from django.contrib import admin
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from Notifi_Service.views import NotificationViewSet

# router = DefaultRouter()
# router.register(r'notifications', NotificationViewSet, basename='notification')

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include(router.urls)),
# ]

from django.contrib import admin
from django.urls import path
from Notifi_Service import views as Notifi_Service
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('notification',Notifi_Service.notification_list)
    path('', Notifi_Service.notification_list, name='notification_list'),
    path('mark_as_read/<int:notification_id>/', Notifi_Service.mark_as_read, name='mark_as_read'),
    path('delete_notification/<int:notification_id>/', Notifi_Service.delete_notification, name='delete_notification'),
]
