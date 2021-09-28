from django.contrib import admin
from .models import (
    CustomUser,
    BursaryCycle, Application, Applicant, Residence
)
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(BursaryCycle)
admin.site.register(Application)
admin.site.register(Applicant)
admin.site.register(Residence)