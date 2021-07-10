from django.contrib import admin

from area.models import District, Division


# Register your models here.
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude', )


class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'division', 'latitude', 'longitude', )
    list_filter = ('division', )


admin.site.register(Division, DivisionAdmin)
admin.site.register(District, DistrictAdmin)
