from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Conversation, Message
from .serializers import MessageSerializer, ConversationSerializer
from openai import OpenAI
import os
import requests

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key= os.getenv("OPENROUTER_API_KEY")
)

def call_ai_api(user_message):
    completion = client.chat.completions.create(
        model="openai/gpt-4o",
        messages=[
            {"role": "user", "content": user_message}
                  ],
                  max_tokens=3000
    )
    return completion.choices[0].message.content


class SendMessageView(APIView):
    def post(self, request):
        conversation_id = request.data.get("conversation_id")
        user_message = request.data.get("message")

        if conversation_id:
            try:
                conversation = Conversation.objects.get(id=conversation_id)
            except Conversation.DoesNotExist:
                return Response({"error": "Conversation not found"}, status=404)
        else:
            first_line = user_message.split("\n")[0][:50]
            conversation = Conversation.objects.create(title=first_line or "New Chat")

        Message.objects.create(
            conversation=conversation,
            sender_type="user",
            content=user_message
        )

        ai_response = call_ai_api(user_message)

        Message.objects.create(
            conversation=conversation,
            sender_type="bot",
            content=ai_response
        )

        return Response({
            "conversation_id": conversation.id,
            "response": ai_response
        }, status=200)
    

class ConversationListView(APIView):
    """List all the conversations the between the user and the ai"""
    def get(self, request):
        conversations = Conversation.objects.all()
        serializer =ConversationSerializer(conversations, many=True)
        return Response(serializer.data)


class ConversationMessageView(APIView):
    """Opens up messages under a previous conversation when the user clicks on chat"""
    def get(self, request, pk):
        try:
            conversation = Conversation.objects.get(id=pk)
        except Conversation.DoesNotExist:
            return Response({"error": "Conversation not found"}, status=404)
        
        messages = conversation.messages.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data, status=200)