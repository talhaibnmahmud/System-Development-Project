from django.contrib import admin

from chat.models import Message


# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ['sender', 'receiver', 'created', ]
    search_fields = ['sender', 'receiver', ]


admin.site.register(Message, MessageAdmin)
