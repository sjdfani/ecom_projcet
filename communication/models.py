from django.db import models
from users.models import CustomUser
from django.utils.translation import ugettext_lazy as _
from products.models import Product


class Message(models.Model):
    from_user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name=_('From user'), related_name='message_from_user'
    )
    to_user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name=_('To user'), related_name='message_to_user'
    )
    message = models.TextField(verbose_name=_('Message'))
    created_at = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name=_('User'), related_name='comment_user'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name=_('Product'), related_name='comment_product'
    )
    comment = models.TextField(verbose_name=_('Comment'))
    created_at = models.DateTimeField(auto_now_add=True)
