from django.urls import path
from bursary_app import views

app_name = 'bursary_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('applicant/register', views.ApplicantRegisterView.as_view(), name='register'),
    path('applicant/login', views.LoginView.as_view(), name='login'),
    path('applicant/profile', views.ApplicantCreateView.as_view(), name='profile'),
    path('applicant/logout', views.LogoutView.as_view(), name='logout'),
]