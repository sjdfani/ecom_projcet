from django.db import models
from users.models import CustomUser
from django.utils.translation import ugettext_lazy as _


class Message(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name=_('User'), related_name='message_user'
    )
    from_user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name=_('From user'), related_name='message_from_user'
    )
    message = models.TextField(verbose_name=_('Message'))
    created_at = models.DateTimeField(auto_now_add=True)
