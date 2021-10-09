from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    CustomUser,
    BursaryCycle, Application, Applicant, Residence
)
# Register your models here.
admin.site.register(CustomUser, UserAdmin)
admin.site.register(BursaryCycle)
admin.site.register(Application)
admin.site.register(Applicant)
admin.site.register(Residence)