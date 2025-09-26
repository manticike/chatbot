#backend/chatbot_api/urls.py
"""Defines URL patterns for chatbot_api"""
from django.urls import path
from .views import SendMessageView, ConversationListView, ConversationMessageView

from . import views

app_name = 'chatbot_api'
urlpatterns = [
    # Home Page
    path('send-message/', SendMessageView.as_view(), name='send-message'),
    path('conversations/', ConversationListView.as_view(), name='conversations'),
    path('conversations/<uuid:pk>/messages/', ConversationMessageView.as_view(), name='conversation-messages'),
]