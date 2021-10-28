from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, views as auth_views
from  django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from bursary_app.models import Applicant, CustomUser
from bursary_app.forms import ApplicantAuthenticationForm, ApplicantRegisterForm
# Create your views here.

@login_required
def dashboard(request):
    """View for an applicant dashboard"""
    return HttpResponse('Welcome to your dashboard')

def index(request):
    """Site home page view"""
    return render(request, 'index.html')

class ApplicantRegisterView(CreateView):
    """Applicant signup view"""
    model = CustomUser
    form_class = ApplicantRegisterForm
    template_name = 'bursary_app/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'applicant'
        return super().get_context_data(**kwargs)
        
    def form_valid(self, form):
        user =form.save()
        login(self.request, user)
        return redirect('bursary_app:profile')

class LoginView(auth_views.LoginView):
    """
    A view that creates an applicant
    """
    template_name = 'bursary_app/login.html'
    authentication_form = ApplicantAuthenticationForm

class LogoutView(auth_views.LogoutView):
    """Applicant logout view"""
    next_page = 'bursary_app:index'

class ApplicantCreateView(LoginRequiredMixin, CreateView):
    """Applicant creation"""
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