from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Message, Comments
from .serializer import (
    MessageSerializer, CreateMessageSerializer, CommentSerializer, CreateCommentSerializer
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


class CreateComments(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateCommentSerializer
    queryset = Comments.objects.all()


class CommentList(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comments.objects.filter(user=self.request.user)
