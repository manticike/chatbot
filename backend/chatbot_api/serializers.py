from rest_framework import serializers
from .models import Conversation, Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender_type', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class ConversationSerializer(serializers.ModelSerializer):
    message = MessageSerializer(many=True, read_only=True, source='message_set')
    class Meta:
        model = Conversation
        fields = ['id', 'title', 'created_at', 'updated_at', 'message']
        read_only_fields = ['id', 'created_at', 'updated_at']