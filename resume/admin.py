from django.contrib import admin
from .models import Resume_info
# Register your models here.

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'dob', 'gender', 'locality', 'city', 'pin_code', 'state', 'mobile', 'email', 'job_city']
admin.site.register(Resume_info, RegistrationAdmin)