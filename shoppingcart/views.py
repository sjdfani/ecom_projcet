from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ShoppingCart
from .serializer import (
    ShoppingCartSerializer, CreateShoppingCartSerializer, UpdateDestroyShoppingCartSerializer,
    PayShoppingCartSerializer,
)


class CreateShoppingCart(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateShoppingCartSerializer
    queryset = ShoppingCart.objects.all()


class ListShoppingCart(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ShoppingCartSerializer

    def get_queryset(self):
        return ShoppingCart.objects.filter(user=self.request.user)


class UpdateDestroyShoppingCart(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ShoppingCartSerializer
        return UpdateDestroyShoppingCartSerializer

    def get_queryset(self):
        return ShoppingCart.objects.filter(user=self.request.user)


class PayShoppingCart(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PayShoppingCartSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
