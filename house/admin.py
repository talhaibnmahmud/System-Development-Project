from django.contrib import admin

from house.models import House, Photo, Favourite


# Register your models here.
class HouseAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('title', 'price', 'category', 'division', 'district', )
    list_filter = ('category', 'created', 'division', )
    list_per_page = 25
    search_fields = ('title', 'address', 'description', )


class PhotoAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('house', 'photo', 'created', )
    list_filter = ('created', )
    list_per_page = 25


class FavouriteAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('house', 'user', 'created', )
    list_filter = ('created', )
    search_fields = ('user', )


admin.site.register(House, HouseAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Favourite, FavouriteAdmin)
