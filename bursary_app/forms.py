from django.forms import forms, ValidationError
from django import forms
from django.contrib.auth.forms import(
    AuthenticationForm,
)
from django.forms.widgets import Widget
from django.utils.translation import gettext_lazy as _

# Bursary app forms
class ApplicantRegisterForm(forms.Form):
    username = forms.CharField(label='Birth Certificate Number', max_length=150)
    first_name = forms.CharField(label='First Name', max_length=150)
    last_name = forms.CharField(label='Last Name', max_length=150)
    password = forms.CharField(label='Create Password', max_length=150, widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Repeat Password', max_length=150, widget=forms.PasswordInput)

class CustomUserCreationForm(forms.Form):
    pass

class CustomUserUpdateform(forms.Form):
    pass

class ApplicantAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if user.is_staff:
            raise ValidationError(
                _('Staff accounts are not allowed to login here'),
                code='no_staff_accounts'
            )