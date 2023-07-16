from datetime import date
from django.conf import settings
from django.db import models

# Create your models here.

class Chat(models.Model):
    created_at = models.DateField(default=date.today)

class Message(models.Model):
    text = models.CharField(max_length=500)
    created_at = models.DateField(default=date.today)
    created_at_time = models.DateTimeField(auto_now_add=True)
    # chat = Chat Klasse verknüpfen
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='chat_message_set', default=None, blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_message_set')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receiver_message_set')