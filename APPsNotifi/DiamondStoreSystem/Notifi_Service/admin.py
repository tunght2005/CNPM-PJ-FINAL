from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'customer_email', 'sent_at', 'is_read')
    list_filter = ('is_read', 'sent_at')
    search_fields = ('title', 'customer_email')

# Form có sẳn
# from django.contrib import admin
# from .models import Notification

# @admin.register(Notification)
# class NotificationAdmin(admin.ModelAdmin):
#     list_display = ('order_code', 'status', 'order_date', 'is_read')
