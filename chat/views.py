from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query_utils import Q
from django.http.response import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from chat.models import Message
from user.models import User


# Create your views here.
class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    context_object_name = 'messages'

    def get_queryset(self):
        # TODO: Get individual user's message
        return Message.objects.filter(Q(sender=self.request.user) | Q(receiver=self.request.user)).order_by('-created')


# TODO: Adding Chat View
class MessageView(LoginRequiredMixin, TemplateView):
    template_name = 'chat/message_page.html'

    def post(self, *args, **kwargs):
        receiver = User.objects.get(username=kwargs.get('pk'))
        message = Message().objects.create(sender=self.request.user, receiver=receiver)

        return HttpResponse(message)
