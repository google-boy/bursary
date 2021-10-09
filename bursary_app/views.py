from django.shortcuts import render
from django.contrib.auth import views as auth_views
from  django.views.generic.edit import CreateView
from bursary_app.models import Applicant
# Create your views here.

def index(request):
    return render(request, 'index.html')

class LoginView(auth_views.LoginView):
    template_name = 'bursary_app/login.html'

