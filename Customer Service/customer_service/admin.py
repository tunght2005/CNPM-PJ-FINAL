from django.contrib import admin
from .models import Customer, PurchaseHistory, Promotion

admin.site.register(Customer)
admin.site.register(PurchaseHistory)
admin.site.register(Promotion)

