# password_histories/utils.py
from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse

from .models import PasswordHistory


def check_password_history(user, new_password):
    """
    desc:
        This util function checks new password with password histories
        cut off by PASSWORD_MATCH_CHECK_UPTO defined in settings
    return:
        Bool
            - True if new password matches with password history
            - False if new password do not matches with password history
    """
    if hasattr(settings, 'PASSWORD_MATCH_CHECK_UPTO'):
        if settings.PASSWORD_MATCH_CHECK_UPTO == 0:
            return HttpResponse(status=500)
        else:
            password_match_check = settings.PASSWORD_MATCH_CHECK_UPTO
    else:
        password_match_check = 3  # default value is 3
    password_histories = PasswordHistory.objects.filter(
        user=user,
    ).order_by('-pk').values_list('password_hash', flat=True)

    if password_histories.count() > password_match_check:
        password_histories = password_histories[:password_match_check]

    for password_histoy in list(password_histories):
        if check_password(new_password, password_histoy):
            return True
    return False
