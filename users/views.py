from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from django.utils import timezone
from .serializer import (
    RegisterUserSerializer, RegisterAdminUserSerializer, LoginSerializer, CustomUserSerializer,
    ForgotPasswordSerializer, VerifyForgotPasswordSerializer, ConfirmForgotPasswordSerializer,
    ChangePasswordSerializer, UpdateInformationSerializer
)
from .permissions import IsSuperuser
from .models import CustomUser
from .utils import get_tokens_for_user


class RegisterUser(CreateAPIView):
    serializer_class = RegisterUserSerializer
    queryset = CustomUser.objects.all()


class RegisterAdminUser(CreateAPIView):
    permission_classes = [IsSuperuser]
    serializer_class = RegisterAdminUserSerializer
    queryset = CustomUser.objects.all()


class Login(APIView):
    def post(self, request):
        serializer = LoginSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = CustomUser.objects.get(email=email)
            user_data = CustomUserSerializer(user)

            if user.check_password(password):
                user.last_login = timezone.now()
                user.save()
                if user.is_superuser:
                    message = {
                        'role': 'manager',
                        'user': user_data.data,
                        'tokens': get_tokens_for_user(user)
                    }
                    return Response(message, status=status.HTTP_200_OK)
                elif user.is_staff and not user.is_superuser:
                    message = {
                        'role': 'admin',
                        'user': user_data.data,
                        'tokens': get_tokens_for_user(user)
                    }
                    return Response(message, status=status.HTTP_200_OK)
                elif user.is_active and not (user.is_superuser and user.is_staff):
                    message = {
                        'role': 'user',
                        'user': user_data.data,
                        'tokens': get_tokens_for_user(user)
                    }
                    return Response(message, status=status.HTTP_200_OK)
            else:
                message = {'message': 'email or password is incorrect'}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)


class ForgotPassword(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


class VerifyForgotPassword(APIView):
    def post(self, request):
        serializer = VerifyForgotPasswordSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            state, message = serializer.save()
            if state:
                return Response(message, status=status.HTTP_200_OK)
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


class ConfirmForgotPassword(APIView):
    def post(self, request):
        serializer = ConfirmForgotPasswordSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


class ChangePassword(APIView):
    def post(self, request):
        serializer = ChangePasswordSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateInformation(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CustomUserSerializer
        return UpdateInformationSerializer

    def get_queryset(self):
        return CustomUser.objects.filter(email=self.request.user.email)


class UserList(ListAPIView):
    permission_classes = [IsSuperuser]
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()


class UserUpdateDestroy(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSuperuser]
    queryset = CustomUser.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CustomUserSerializer
        return UpdateInformationSerializer
