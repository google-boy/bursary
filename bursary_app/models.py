from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from tree.fields import PathField
from tree.models import TreeModelMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.mail import send_mail
# Create your models here.

class Applicant(models.Model):
    """
    Model for student basic details.
    """
    birth_cert_number = models.CharField(
        'Birth certificate number',
        primary_key=True,
        max_length=20
    )
    id_number = models.IntegerField(null=True, blank=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    other_name = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=6)
    admission_no = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.birth_cert_number}'

class ParentalStatus(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.RESTRICT)
    parent = models.ForeignKey('Parent', null=True, on_delete=models.SET_NULL)
    parental_status = models.CharField(max_length=50)
    relationship = models.CharField(max_length=50)

class ApplicantResidence(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.RESTRICT)
    residence = models.ForeignKey('Residence', null=True, on_delete=models.SET_NULL)

class ApplicantInstitution(models.Model):
    student = models.ForeignKey(Applicant, on_delete=models.RESTRICT)
    institution = models.ForeignKey('LearningInstitution', null=True, on_delete=models.SET_NULL)
    year_of_study = models.PositiveIntegerField()

class Parent(models.Model):
    """
    Model for parent or guardian details.
    """
    id_number = models.PositiveIntegerField(unique=True, null=True, blank=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    other_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=6)
    alive = models.BooleanField()
    death_cert_no = models.CharField(
        'death certificate number',
        null=True, blank=True,
        max_length=20
    )
    applicant_parent = models.ManyToManyField(Applicant, through=ParentalStatus)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

class ParentAddress(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)

class ParentContact(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    contact = models.ForeignKey('Contact', on_delete=models.CASCADE)

class Sibling(models.Model):
    """
    Model for sibling details.
    """
    birth_cert_number = models.CharField(
        'Birth certificate number',
        max_length=20
    )
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    other_name = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=6)
    learning_institution = models.ForeignKey('LearningInstitution', null=True, on_delete=models.SET_NULL)
    admission_no = models.CharField(max_length=50)
    applicant = models.ManyToManyField(Applicant)

    def __str__(self) -> str:
        return f'{self.last_name} {self.first_name}'

class Residence(models.Model, TreeModelMixin):
    """
    Model for residential details.
    """
    name = models.CharField('Name of administrative unit', max_length=100)
    parent =  models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    path = PathField()

    def __str__(self) -> str:
        return self.name

class LearningInstitution(models.Model):
    """
    Model for learning institution details
    """
    name = models.CharField(
        'Institution name',
        max_length=250
    )
    type = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name}'

class Bank(models.Model):
    institution = models.ForeignKey(LearningInstitution, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    branch = models.CharField(max_length=250)
    account_name = models.CharField(max_length=250)
    account_number = models.PositiveBigIntegerField()

    def __str__(self):
        return self.account_name

class InstitutionAddress(models.Model):
    institution = models.ForeignKey(LearningInstitution, on_delete=models.CASCADE)
    address = models.ForeignKey('Address', null=True, on_delete=models.SET_NULL)

class InstitutionContact(models.Model):
    institution = models.ForeignKey(LearningInstitution, on_delete=models.CASCADE)
    contact = models.ForeignKey('Contact', null=True, on_delete=models.SET_NULL)

class Address(models.Model):
    """
    Model for postal addresses
    """
    postal_address = models.IntegerField()
    postal_code = models.IntegerField()
    city = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.postal_address} - {self.postal_code}, {self.city}'

class Contact(models.Model):
    """
    Model for contacts
    """
    phone_number = PhoneNumberField()
    email_address = models.EmailField(null=True, blank=True)
    telephone = PhoneNumberField(max_length=15, null=True, blank=True)

class BursaryCycle(models.Model):
    fiscal_year = models.CharField(max_length=10)
    allocation = models.PositiveBigIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.fiscal_year
    
class Application(models.Model):
    """
    Model for bursary application cycle.
    """
    application_cycle = models.OneToOneField(BursaryCycle, on_delete=models.RESTRICT)
    applicant = models.ForeignKey(Applicant, on_delete=models.RESTRICT)
    successful = models.BooleanField()
    remarks = models.TextField('comment', null=True, blank=True)
    amount = models.DecimalField('amount awarded', max_digits=7, decimal_places=2)

    def __str__(self) -> str:
        return self.application_cycle

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user inheriting from AbstractBaseUser, PermisionsMixin
    """
    username_validator = ASCIIUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)