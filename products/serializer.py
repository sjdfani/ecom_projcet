from rest_framework import serializers

from .models import Category, Warranty, Product, Favorite


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class WarrantySerializer(serializers.ModelSerializer):
    class Meta:
        model = Warranty
        fields = '__all__'


class FavoriteProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class CreateFavoriteProductSerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all()
    )

    def create(self, validated_data):
        user = self.context['request'].user
        product = validated_data['product']
        return Favorite.objects.create(user=user, product=product)
