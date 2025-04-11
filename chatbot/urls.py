from django.urls import path
from .views import chatbot_ui, chat #,chatbot_response,chatbot_view # Import the new home view

urlpatterns = [
    path('', chatbot_ui, name='chatbot_ui'),  # Home page
    path('api/chat/', chat, name='chat'),  # Chatbot API
#     path("chatbot/", chatbot_response, name="chatbot_response"),
#      path("chatbot/", chatbot_view, name="chatbot_api"),
]
