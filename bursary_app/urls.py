from django.urls import path
from bursary_app import views

app_name = 'bursary_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('profile', views.ApplicantProfileView.as_view(), name='profile'),
    path('register', views.ApplicantRegisterView.as_view(), name='register'),
    path('login', views.LoginView.as_view(), name='login'),
    path('profile/edit', views.ApplicantCreateView.as_view(), name='edit_profile'),
    path('logout', views.LogoutView.as_view(), name='logout'),
]