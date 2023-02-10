from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import (
    RegisterUserSerializer, RegisterAdminUserSerializer
)
from .permissions import IsSuperuser


class RegisterUser(APIView):
    def post(self, request):
        serializer = RegisterUserSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            message = {'create-user': 'create is successful'}
            return Response(message, status=status.HTTP_201_CREATED)


class RegisterAdminUser(APIView):
    permission_classes = [IsSuperuser]

    def post(self, request):
        serializer = RegisterAdminUserSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            message = {'create-admin': 'create is successful'}
            return Response(message, status=status.HTTP_201_CREATED)
