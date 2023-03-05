from django import forms
from django.contrib.auth.forms import PasswordChangeForm as BasePasswordChangeForm

class PasswordChangeForm(BasePasswordChangeForm):
    """
    A form that lets a user change their password by entering their old password
    and a new password.
    """
    old_password = forms.CharField(
        label= False,
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True, 'placeholder':'Current password', 'class': 'passReset'}),
    )
    new_password1 = forms.CharField(
        label=False,
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'placeholder':'New password', 'class': 'passReset'}),
    )
    new_password2 = forms.CharField(
        label=False,
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'placeholder':'New password confirmation', 'class': 'passReset'}),
    )