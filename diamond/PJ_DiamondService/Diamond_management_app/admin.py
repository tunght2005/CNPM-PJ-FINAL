from django.contrib import admin
from .models import diamond
# Register your models here.

class DiamondAdmin(admin.ModelAdmin):
  list_display = ("DiaName", "carat", "shape", 'cut', 'color', 'clarity', 'DiamondPrice', 'UpdatedDate')
  
admin.site.register(diamond, DiamondAdmin)