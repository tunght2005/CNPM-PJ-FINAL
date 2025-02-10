from django.contrib import admin
from .models import Notification
# Register your models here.
# admin.site.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'status', 'order_date', 'active')
admin.site.register(Notification, NotificationAdmin)