from rest_framework import serializers
from .models import CustomUser
from .utils import number_generator
from ecom_project.settings import Redis_object


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


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError('this email is not exists')
        return value

    def process(self, validated_data):
        email = validated_data['email']
        code = number_generator(6)
        Redis_object.set(email, code, ex=360)
        # send code to email
        print(f"forgot password code: {code}")

    def save(self, **kwargs):
        self.process(self.validated_data)


class VerifyForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)

    def validate_email(self, value):
        if not CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError('this email is not exists')
        return value

    def process(self, validated_data):
        email = validated_data['email']
        code = validated_data['code']
        redis_code = Redis_object.get(email)
        if redis_code:
            if redis_code == code:
                return (True, {'message': 'code is correct'})
            else:
                return (False, {'message': 'code is incorrect'})
        return (False, {'message': 'code has expired'})

    def save(self, **kwargs):
        return self.process(self.validated_data)


class ConfirmForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=20, write_only=True)

    def validate_email(self, value):
        if not CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError('this email is not exists')
        return value

    def process(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        user = CustomUser.objects.get(email=email)
        user.set_password(password)
        user.save()

    def save(self, **kwargs):
        self.process(self.validated_data)


class ChangePasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    old_password = serializers.CharField(max_length=20, write_only=True)
    new_password = serializers.CharField(max_length=20, write_only=True)

    def validate(self, attrs):
        user = CustomUser.objects.filter(email=attrs['email'])
        if not user.exists():
            raise serializers.ValidationError(
                {'email': 'this email is not exists'})
        if not user.first().check_password(attrs['old_password']):
            raise serializers.ValidationError(
                {'password': 'your old password is incorrect'})
        return attrs

    def process(self, validated_data):
        email = validated_data['email']
        new_password = validated_data['new_password']
        user = CustomUser.objects.get(email=email)
        user.set_password(new_password)
        user.save()

    def save(self, **kwargs):
        self.process(self.validated_data)


class UpdateInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'fullname', 'phone', 'home', 'address', 'gender', 'national_code', 'birthdate', 'get_newsletter')
