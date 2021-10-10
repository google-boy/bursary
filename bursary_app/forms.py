from django.forms import forms, ValidationError
from django.contrib.auth.forms import(
    AuthenticationForm,
)
from django.utils.translation import gettext_lazy as _

# Bursary app forms
class ApplicantCreationForm(forms.Form):
    pass

class CustomUserCreationForm(forms.Form):
    pass

class CustomUserUpdateform(forms.Form):
    pass

class ApplicantAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user) -> None:
        super().confirm_login_allowed(user)
        if not user.is_applicant:
            raise ValidationError(
                _('Staff accounts are not allowed to login here'),
                code='no_staff_accounts'
            )