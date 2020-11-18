from django.contrib import admin

from .models import Condition
from .models import Tractor
from .models import Equipment

# Register your models here.

class ConditionAdmin(admin.ModelAdmin):
    list_display = ['description']
    # empty_value_display = '-empty-'
    # list_filter = ['description']
    list_per_page = 25
    ordering = ['description']

admin.site.register(Condition, ConditionAdmin)

class TractorAdmin(admin.ModelAdmin):
    list_display = ['id', 'make', 'model', 'price', 'year', 'condition', 'hours', 'engine_power', 'fuel_type']
    # empty_value_display = '-empty-'
    list_filter = ['make', 'condition', 'fuel_type']
    list_per_page = 25
    ordering = ['id', 'price', 'year', 'hours', 'engine_power']

admin.site.register(Tractor, TractorAdmin)

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['tractor', 'name']
    # empty_value_display = '-empty-'
    list_filter = ['tractor', 'name']
    list_per_page = 25
    ordering = ['tractor', 'name']

admin.site.register(Equipment, EquipmentAdmin)