from rest_framework import serializers
from .models import ShoppingCart, ShoppingcartStatus
from products.serializer import ProductSerializer, CouponSerializer
from django.utils import timezone


class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = '__all__'

    def to_representation(self, instance):
        request = self.context['request']
        res = super().to_representation(instance)
        res['product'] = ProductSerializer(
            instance.product, context={'request': request}
        ).data
        res['coupon'] = CouponSerializer(
            instance.coupon, context={'request': request}
        ).data
        return res


class CreateShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        exclude = ('tracking_number', 'paid_date', 'bank_name', 'user')

    def create(self, validated_data):
        user = self.context['request'].user
        obj = ShoppingCart.objects.create(user=user, **validated_data)
        return obj


class UpdateDestroyShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        exclude = (
            'user', 'product', 'bank_name', 'tracking_number', 'paid_date')


class PayShoppingCartSerializer(serializers.Serializer):
    shoppingcart_id = serializers.PrimaryKeyRelatedField(
        queryset=ShoppingCart.objects.all()
    )
    bank_name = serializers.CharField(max_length=100)
    tracking_number = serializers.CharField(max_length=100)

    def process(self, validated_data):
        shoppingcart = validated_data['shoppingcart_id']
        shoppingcart.bank_name = validated_data['bank_name']
        shoppingcart.tracking_number = validated_data['tracking_number']
        shoppingcart.paid_date = timezone.now()
        shoppingcart.status = ShoppingcartStatus.DONE
        shoppingcart.save()

    def save(self, **kwargs):
        self.process(self.validated_data)
