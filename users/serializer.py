from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ('password',)


class RegisterUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=20, write_only=True)

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError('this email is taken')
        return value

    def save(self, **kwargs):
        email = self.validated_data['email']
        password = self.validated_data['password']
        user = CustomUser.objects.create(email=email, password=password)
        user.set_password(password)
        user.save()


class RegisterAdminUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=20, write_only=True)

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError('this email is taken')
        return value

    def save(self, **kwargs):
        email = self.validated_data['email']
        password = self.validated_data['password']
        user = CustomUser.objects.create(email=email, password=password)
        user.set_password(password)
        user.is_staff = True
        user.save()


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=20)

    def validate_email(self, value):
        if not CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError('this email is not exists')
        return value
