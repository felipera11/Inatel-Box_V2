# core/admin.py
from django.contrib import admin
from .models import PrintModel

@admin.register(PrintModel)
class PrintModelAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'user', 'material', 'infill_percentage', 'layer_height', 'submitted_at', 'is_completed', 'budget')
    list_filter = ('material', 'is_completed')
    search_fields = ('model_name', 'user__username')
    ordering = ('-submitted_at',)
