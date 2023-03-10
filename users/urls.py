from django.urls import path
from .views import (
    RegisterUser, RegisterAdminUser, Login, ForgotPassword, VerifyForgotPassword, ConfirmForgotPassword,
    ChangePassword, UpdateInformation, UserList, UserUpdateDestroy
)

app_name = 'users'

urlpatterns = [
    path('register-user/', RegisterUser.as_view(), name='register-user'),
    path('register-admin/', RegisterAdminUser.as_view(), name='register-admin'),
    path('login/', Login.as_view(), name='login'),
    path('forgot-password/', ForgotPassword.as_view(), name='forgot-password'),
    path('verify-forgot-password/', VerifyForgotPassword.as_view(),
         name='verify-forgot-password'),
    path('confirm-forgot-password/', ConfirmForgotPassword.as_view(),
         name='confirm-forgot-password'),
    path('change-password/', ChangePassword.as_view(), name='change-password'),
    path('update-information/<int:pk>/',
         UpdateInformation.as_view(), name='update-information'),
    path('list/', UserList.as_view(), name='user-list'),
    path('list/<int:pk>/', UserUpdateDestroy.as_view(), name='user-information'),
]
