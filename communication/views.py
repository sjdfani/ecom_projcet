from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Message
from .serializer import (
    MessageSerializer, CreateMessageSerializer
)


class CreateMessage(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateMessageSerializer
    queryset = Message.objects.all()


class MessageList(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.filter(to_user=self.request.user)
