# password_histories/admin.py
from django.conf import settings
from django.contrib import admin

from .models import PasswordHistory


admin.site.register(PasswordHistory)
