from django.contrib import admin

from .models import Make
from .models import Condition
from .models import Tractor
from .models import Equipment

# Register your models here.

class MakeAdmin(admin.ModelAdmin):
    list_display = ['name']
    # empty_value_display = '-empty-'
    # list_filter = ['name']
    list_per_page = 25
    ordering = ['name']

admin.site.register(Make, MakeAdmin)

class ConditionAdmin(admin.ModelAdmin):
    list_display = ['description']
    # empty_value_display = '-empty-'
    # list_filter = ['description']
    list_per_page = 25
    ordering = ['description']

admin.site.register(Condition, ConditionAdmin)

admin.site.register(Tractor)

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['tractor', 'name']
    # empty_value_display = '-empty-'
    list_filter = ['tractor', 'name']
    list_per_page = 25
    ordering = ['tractor', 'name']

admin.site.register(Equipment, EquipmentAdmin)