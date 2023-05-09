from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Employee


admin.site.register(Employee, MPTTModelAdmin)
# admin.site.register(Employee)