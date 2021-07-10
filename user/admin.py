from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.forms import CustomUserCreationForm
from user.models import User


# Register your models here.
class Admin(UserAdmin):
    add_form = CustomUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Extra Fields',
            {
                'fields': ('phone', ),
            },
        ),
    )

    list_display = ('username', 'email', 'phone')


admin.site.site_header = 'RentalBD Administration'
admin.site.site_title = 'RentalBD Admin Site'
admin.site.index_title = 'RentalBD Admin Panel'

admin.site.register(User, Admin)
