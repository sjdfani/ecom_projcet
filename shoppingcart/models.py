from django.db import models
from users.models import CustomUser
from products.models import Product, Coupon
from django.utils.translation import ugettext_lazy as _


class ShoppingcartStatus(models.TextChoices):
    DONE = ('done', 'Done')
    IN_PROGRESS = ('in_progress', 'In_progress')
    WAITING = ('waiting', 'Waiting')
    FAILED = ('failed', 'Failed')


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name=_('User'), related_name='shoppingcart_user'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name=_('Product'), related_name='shoppingcart_product'
    )
    count = models.IntegerField(default=1, verbose_name=_('Count'))
    tracking_number = models.CharField(
        max_length=100, verbose_name=_('Tracking Number'), null=True, blank=True
    )
    bank_name = models.CharField(
        max_length=100, verbose_name=_('Bank Name'), null=True, blank=True
    )
    paid_date = models.DateTimeField(
        verbose_name=_('Paid Date'), null=True, blank=True
    )
    coupon = models.ForeignKey(
        Coupon, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('Coupon'), related_name='shoppingcart_coupon'
    )
    status = models.CharField(
        max_length=15, choices=ShoppingcartStatus.choices, default=ShoppingcartStatus.WAITING, verbose_name=_('Shopping Cart Status')
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.email
