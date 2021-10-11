from django.contrib import admin

class CustomAdminSite(admin.AdminSite):
    site_header = 'Bursary Administration'
    site_title = 'Bursary site Admin'