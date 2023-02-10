from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from .serializer import (
    RegisterUserSerializer, RegisterAdminUserSerializer, LoginSerializer, CustomUserSerializer
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
