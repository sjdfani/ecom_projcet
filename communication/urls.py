from django.urls import path
from .views import (
    MessageList, CreateMessage
)

app_name = 'communication'

urlpatterns = [
    path('message/create/', CreateMessage.as_view(), name='create-message'),
    path('message/list/', MessageList.as_view(), name='message-list'),
]
