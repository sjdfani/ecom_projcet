from rest_framework import serializers
from .models import Message, Comments
from users.models import CustomUser
from users.serializer import CustomUserSerializer
from products.models import Product
from products.serializer import ProductSerializer


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


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

    def to_representation(self, instance):
        request = self.context['request']
        res = super().to_representation(instance)
        res['user'] = CustomUserSerializer(
            instance.user, context={'request': request}
        ).data
        res['product'] = ProductSerializer(
            instance.product, context={'request': request}
        ).data
        return res


class CreateCommentSerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all()
    )
    comment = serializers.CharField(max_length=200)

    def create(self, validated_data):
        user = self.context['request'].user
        product = validated_data['product']
        comment = validated_data['comment']
        obj = Comments.objects.create(
            user=user, product=product, comment=comment)
        return obj
