from django.contrib import admin

# Register your models here.
from .models import GlobalConstant


class GlobalConstantAdmin(admin.ModelAdmin):
    list_display = ["key", "key_type", "value"]


admin.site.register(GlobalConstant, GlobalConstantAdmin)
