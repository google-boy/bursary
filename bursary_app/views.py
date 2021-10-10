from django.shortcuts import render
from django.contrib.auth import views as auth_views
from  django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from bursary_app.models import Applicant
from bursary_app.forms import ApplicantAuthenticationForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

class LoginView(auth_views.LoginView):
    template_name = 'bursary_app/login.html'
    authentication_form = ApplicantAuthenticationForm

class ApplicantCreateView(LoginRequiredMixin, CreateView):
    model = Applicant
    fields = [
        'birth_cert_number',
        'admission_no',
        'id_number',
        'first_name',
        'last_name',
        'other_name',
        'date_of_birth',
        'gender'
    ]