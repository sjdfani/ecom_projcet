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


class FavoriteProductDestroySerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all()
    )

    def validate(self, attrs):
        user = self.context['request'].user
        product = attrs['product']
        if not Favorite.objects.filter(user=user, product=product).exists():
            raise serializers.ValidationError(
                {'favorite': 'this item is not exists'})
        return attrs

    def process(self, validated_data):
        user = self.context['request'].user
        product = validated_data['product']
        obj = Favorite.objects.get(user=user, product=product)
        obj.delete()

    def save(self, **kwargs):
        self.process(self.validated_data)


class CreateFavoriteProductSerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all()
    )

    def create(self, validated_data):
        user = self.context['request'].user
        product = validated_data['product']
        return Favorite.objects.create(user=user, product=product)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        request = self.context['request']
        res = super().to_representation(instance)
        res['warranty'] = WarrantySerializer(
            instance.warranty, context={'request': request}
        ).data
        res['category'] = CategorySerializer(
            instance.category, context={'request': request}
        ).data
        return res


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('user',)

    def create(self, validated_data):
        user = self.context['request'].user
        return Product.objects.create(user=user, **validated_data)
