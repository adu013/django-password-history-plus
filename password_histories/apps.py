# password_histories/apps.py
from django.apps import AppConfig


class PasswordHistoriesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "password_histories"

    def ready(self):
        import password_histories.signals
