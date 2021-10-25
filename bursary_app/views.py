from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView, View
from  django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from bursary_app.models import Applicant
from bursary_app.forms import ApplicantAuthenticationForm, ApplicantRegisterForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

class ApplicantRegisterView(View):
    template_name = 'bursary_app/register.html'
    form_class = ApplicantRegisterForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        ...

class LoginView(auth_views.LoginView):
    template_name = 'bursary_app/login.html'
    authentication_form = ApplicantAuthenticationForm

class LogoutView(auth_views.LogoutView):
    next_page = 'bursary_app:index'

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