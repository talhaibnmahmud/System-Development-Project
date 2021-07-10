from django.urls.conf import path

from chat.views import MessageListView, MessageView


app_name = 'chat'

urlpatterns = [
    path('', MessageListView.as_view(), name='message-home'),
    path('<slug:pk>/', MessageView.as_view(), name='message'),
]
