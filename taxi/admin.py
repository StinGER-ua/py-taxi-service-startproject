from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Driver, Manufacturer, Car


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number", )
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number", )}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("license_number",
                                        "first_name",
                                        "last_name")}
         ),
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["model", "manufacturer"]
    search_fields = ["model"]
    list_filter = ["manufacturer"]


@admin.register(Manufacturer)
class Manufacturer(admin.ModelAdmin):
    list_display = ["name", "country"]
    list_filter = ["country"]