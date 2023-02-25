# password_histories/signals.py
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import pre_save

from .models import PasswordHistory

User = get_user_model()


"""
Desc:
    Check if password is changed
    If password is changed, then store old password
"""
@receiver(pre_save, sender=User)
def save_password_history(sender, **kwargs):
    user = kwargs.get('instance', None)
    if user:
        new_password = user.password

        try:
            old_password = User.objects.get(pk=user.pk).password
        except User.DoesNotExist:
            old_password = None

        # when password is changed
        if new_password != old_password:

            # store old password
            if old_password:
                PasswordHistory.objects.create(
                    user=user,
                    password_hash=old_password
                )
