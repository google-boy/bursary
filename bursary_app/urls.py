from django.urls import path
from . import views

app_name = 'bursary_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('applicant/login', views.LoginView.as_view(), name='login'),
    ]
