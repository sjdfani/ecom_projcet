from django.urls import path
from .views import (
    MessageList, CreateMessage, CommentList, CreateComments, CommentListByProduct
)

app_name = 'communication'

urlpatterns = [
    path('message/create/', CreateMessage.as_view(), name='create-message'),
    path('message/list/', MessageList.as_view(), name='message-list'),
    path('comment/create/', CreateComments.as_view(), name='create-comment'),
    path('comment/list/', CommentList.as_view(), name='comment-list'),
    path('comment/list/product=<int:id>/',
         CommentListByProduct.as_view(), name='comment-list-product'),
]
