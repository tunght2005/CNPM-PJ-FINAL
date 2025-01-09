from django.contrib import admin # type: ignore
from .models import user, PaymentMethod, TransactionHistory, Notification

# Register your models here.
#admin.site.register(user)
#admin.site.register(PaymentMethod)
#admin.site.register(TransactionHistory)
#admin.site.register(Notification)

class userAdmin(admin.ModelAdmin):
      list_display = ("Username", "Userid", "UserPhone",)
class PaymentMethodAdmin(admin.ModelAdmin):
      list_display = ("User", "Details",)
class TransactionHistoryAdmin(admin.ModelAdmin):
      list_display = ("User", "PaymentMethod", "Amount",)
class NotificationAdmin(admin.ModelAdmin):
      list_display = ("User", "Message", "CreatedAt",)
admin.site.register(user, userAdmin)
admin.site.register(PaymentMethod, PaymentMethodAdmin)
admin.site.register(TransactionHistory, TransactionHistoryAdmin)
admin.site.register(Notification, NotificationAdmin)