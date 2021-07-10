from django.contrib import admin

from contact.models import Contact


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'created', )
    search_fields = ('name', 'phone', 'email', )


admin.site.register(Contact, ContactAdmin)
