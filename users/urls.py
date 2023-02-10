from django.urls import path
from .views import (
    RegisterUser, RegisterAdminUser
)

app_name = 'users'

urlpatterns = [
    path('register-user/', RegisterUser.as_view(), name='register-user'),
    path('register-admin/', RegisterAdminUser.as_view(), name='register-admin'),
]
