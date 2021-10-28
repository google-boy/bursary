from django.db import transaction
from django.forms import ValidationError
from bursary_app.models import Applicant, CustomUser
from django.contrib.auth.forms import(
    AuthenticationForm, UserCreationForm
)
from django.utils.translation import gettext_lazy as _

# Bursary app forms
class ApplicantRegisterForm(UserCreationForm):
    """
    A form that creates an applicant as a user of the system.
    """
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_applicant = True
        user.save()
        #Applicant.objects.create(user=user)
        return user

class ApplicantAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if user.is_staff:
            raise ValidationError(
                _('Staff accounts are not allowed to login here'),
                code='no_staff_accounts'
            )