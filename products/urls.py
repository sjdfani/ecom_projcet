from django.urls import path
from .views import (
    CategoryList, CreateCategory, WarrantyList, CreateWarranty, CreateFavoriteProduct,
    FavoriteProductList, FavoriteProductDestroy, CreateProduct, ProductList, UpdateProduct,
    CreateCoupon, CouponList
)

app_name = 'products'

urlpatterns = [
    path('category/create/', CreateCategory.as_view(), name='create-category'),
    path('category/list/', CategoryList.as_view(), name='category-list'),
    path('warranty/create/', CreateWarranty.as_view(), name='create-warranty'),
    path('warranty/list/', WarrantyList.as_view(), name='warranty-list'),
    path('favorite/create/', CreateFavoriteProduct.as_view(), name='favorite-create'),
    path('favorite/list/', FavoriteProductList.as_view(), name='favorite-list'),
    path('favorite/delete/', FavoriteProductDestroy.as_view(),
         name='favorite-destroy'),
    path('product/create/', CreateProduct.as_view(), name='create-product'),
    path('product/list/', ProductList.as_view(), name='product-list'),
    path('product/list/<int:pk>/', UpdateProduct.as_view(), name='product-update'),
    path('coupon/create/', CreateCoupon.as_view(), name='create-coupon'),
    path('coupon/list/', CouponList.as_view(), name='coupon-list'),
]
