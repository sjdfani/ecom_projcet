from django.urls import path
from .views import (
    CreateShoppingCart, ListShoppingCart, UpdateDestroyShoppingCart, PayShoppingCart,
)

app_name = 'shoppingcart'

urlpatterns = [
    path('create/', CreateShoppingCart.as_view(), name='create-shoppingcart'),
    path('list/', ListShoppingCart.as_view(), name='list-shoppingcart'),
    path('list/<int:pk>/', UpdateDestroyShoppingCart.as_view(),
         name='update-shoppingcart'),
    path('pay/', PayShoppingCart.as_view(), name='pay-shoppingcart'),
]
