from rest_framework import serializers
from .models import Message
from users.models import CustomUser
from users.serializer import CustomUserSerializer


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

    def to_representation(self, instance):
        request = self.context['request']
        res = super().to_representation(instance)
        res['from_user'] = CustomUserSerializer(
            instance.from_user, context={'request': request}
        ).data
        return res


class CreateMessageSerializer(serializers.Serializer):
    to_user = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all()
    )
    message = serializers.CharField(max_length=200)

    def create(self, validated_data):
        from_user = self.context['request'].user
        to_user = validated_data['to_user']
        message = validated_data['message']
        obj = Message.objects.create(
            from_user=from_user, to_user=to_user, message=message)
        return obj
