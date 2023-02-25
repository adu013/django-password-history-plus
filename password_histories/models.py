# password_histories/models.py

from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class PasswordHistory(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user"
    )
    password_hash = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        default=""
    )

    def __str__(self):
        if self.user.username:
            return "id: {}, user: {}".format(self.pk, self.user.username)
        else:
            return "id: {}".format(self.pk)
