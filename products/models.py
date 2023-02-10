from django.db import models
from django.utils.translation import ugettext_lazy as _
from users.models import CustomUser


class Warranty(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True, verbose_name=_('User'), related_name='product_user'
    )
    warranty = models.ForeignKey(
        Warranty, on_delete=models.SET_NULL, null=True, verbose_name=_('warranty'), related_name='product_warranty'
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, verbose_name=_('category'), related_name='product_category'
    )
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    description = models.TextField(
        verbose_name=_('Description'), null=True, blank=True)
    image_1 = models.ImageField(
        upload_to='product/images/', verbose_name=_('Image 1'), null=True, blank=True)
    image_2 = models.ImageField(
        upload_to='product/images/', verbose_name=_('Image 2'), null=True, blank=True)
    image_3 = models.ImageField(
        upload_to='product/images/', verbose_name=_('Image 3'), null=True, blank=True)
    image_4 = models.ImageField(
        upload_to='product/images/', verbose_name=_('Image 4'), null=True, blank=True)
    color = models.CharField(
        max_length=20, verbose_name=_('Color'), null=True, blank=True)
    material = models.CharField(
        max_length=50, verbose_name=_('Material'), null=True, blank=True)
    price = models.BigIntegerField(default=0, verbose_name=_('Price'))
    status = models.BooleanField(default=False, verbose_name=_('Status'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Favorite(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name=_('User'), related_name='favorite_user'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name=_('Product'), related_name='favorite_product'
    )
    created_at = models.DateTimeField(auto_now_add=True)


class CouponStatus(models.TextChoices):
    AVAILABLE = ('available', 'Available')
    USED = ('used', 'Used')
    EXPIRE = ('expire', 'Expire')


class Coupon(models.Model):
    created_by = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name=_('created_by user')
    )
    discount = models.IntegerField(
        default=0, verbose_name=_('Discount (percent)'))
    expiration_time = models.DateTimeField(verbose_name=_('Expiration time'))
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10, choices=CouponStatus.choices, default=CouponStatus.AVAILABLE, verbose_name=_('status')
    )
