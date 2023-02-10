from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Favorite, Warranty, Product, Coupon
from .permissions import IsSuperuserORAdmin
from .serializer import (
    CategorySerializer, WarrantySerializer, CreateFavoriteProductSerializer, FavoriteProductSerializer,
    CreateProductSerializer, ProductSerializer, FavoriteProductDestroySerializer, CreateCouponSerializer,
    CouponSerializer,
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


class FavoriteProductList(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FavoriteProductSerializer

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)


class FavoriteProductDestroy(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = FavoriteProductDestroySerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)


class CreateProduct(CreateAPIView):
    permission_classes = [IsSuperuserORAdmin]
    serializer_class = CreateProductSerializer
    queryset = Product.objects.all()


class ProductList(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class UpdateProduct(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSuperuserORAdmin]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class CreateCoupon(CreateAPIView):
    permission_classes = [IsSuperuserORAdmin]
    serializer_class = CreateCouponSerializer
    queryset = Coupon.objects.all()


class CouponList(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CouponSerializer

    def get_queryset(self):
        return Coupon.objects.filter(user=self.request.user)
