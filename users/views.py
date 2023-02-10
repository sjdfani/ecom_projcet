from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from .serializer import (
    RegisterUserSerializer, RegisterAdminUserSerializer
)
from .permissions import IsSuperuser
from .models import CustomUser


class RegisterUser(CreateAPIView):
    serializer_class = RegisterUserSerializer
    queryset = CustomUser.objects.all()


class RegisterAdminUser(CreateAPIView):
    permission_classes = [IsSuperuser]
    serializer_class = RegisterAdminUserSerializer
    queryset = CustomUser.objects.all()
