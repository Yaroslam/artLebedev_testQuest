from django.contrib import admin
from .models.CertifiedSpecialist import CertifiedSpecialist

@admin.register(CertifiedSpecialist)
class MenuAdmin(admin.ModelAdmin):
    list_display = (['fio'])