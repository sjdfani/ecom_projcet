from django.urls import path
from .views import (
    CategoryList, CreateCategory, WarrantyList, CreateWarranty, CreateFavoriteProduct,
    FavoriteProductList, FavoriteProductDestroy
)

app_name = 'products'

urlpatterns = [
    path('category/create/', CreateCategory.as_view(), name='create-category'),
    path('category/list/', CategoryList.as_view(), name='category-list'),
    path('warranty/create/', CreateWarranty.as_view(), name='create-warranty'),
    path('warranty/list/', WarrantyList.as_view(), name='warranty-list'),
    path('favorite/create/', CreateFavoriteProduct.as_view(), name='favorite-create'),
    path('favorite/list/', FavoriteProductList.as_view(), name='favorite-list'),
    path('favorite/delete/<int:pk>/', FavoriteProductDestroy.as_view(),
         name='favorite-destroy'),
]
