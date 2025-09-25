# chatbot_api/models.py
import uuid
from django.db import models

# Create your models here.
class Conversation(models.Model):
    """Storing conversations for each session"""
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'conversation'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['id', 'created_at']),
            models.Index(fields=['updated_at']),
        ]

    def __str__(self):
        """Return a string representation of the model"""
        return f"{self.title} ({self.id})"
    

class Message(models.Model):
    """Messages between chatbot and the user(human)"""
    SENDER_CHOICES= [
        ("user", "User"),
        ("bot", "Bot"),
    ]
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    conversation = models.ForeignKey(Conversation, related_name="messages", on_delete=models.CASCADE)
    sender_type = models.CharField(max_length=10, choices=SENDER_CHOICES)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'message'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['id', 'created_at']),
            models.Index(fields=['updated_at']),
        ]

    def __str__(self):
        return f"{self.sender_type} ({self.content[:30]}) ({self.id})"

