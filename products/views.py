from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Category, Favorite, Warranty, Product
from .permissions import IsSuperuserORAdmin
from .serializer import (
    CategorySerializer, WarrantySerializer, CreateFavoriteProductSerializer, FavoriteProductSerializer,

)


class CreateCategory(CreateAPIView):
    permission_classes = [IsSuperuserORAdmin]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryList(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CreateWarranty(CreateAPIView):
    permission_classes = [IsSuperuserORAdmin]
    serializer_class = WarrantySerializer
    queryset = Warranty.objects.all()


class WarrantyList(ListAPIView):
    serializer_class = WarrantySerializer
    queryset = Warranty.objects.all()


class CreateFavoriteProduct(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateFavoriteProductSerializer
    queryset = Favorite.objects.all()


class FavoriteProductList(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FavoriteProductSerializer

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)


class FavoriteProductDestroy(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FavoriteProductSerializer

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)
