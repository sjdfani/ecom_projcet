from django.urls import path
from .views import (
    RegisterUser, RegisterAdminUser, Login
)

app_name = 'users'

urlpatterns = [
    path('register-user/', RegisterUser.as_view(), name='register-user'),
    path('register-admin/', RegisterAdminUser.as_view(), name='register-admin'),
    path('login/', Login.as_view(), name='login'),
]
