from django.db import models

from user.models import User


# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    # TODO: mark editable = False

    def __str__(self):
        return f'From - {self.sender.username} \t To - {self.receiver.username}'
