#backend/chatbot_api/urls.py
"""Defines URL patterns for chatbot_api"""

from django.urls import path

from . import views

app_name = 'chatbot_api'
urlpatterns = [
    # Home Page
    path('', views)
]