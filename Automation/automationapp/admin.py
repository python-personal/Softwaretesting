from django.contrib import admin
from automationapp.models import *
# Register your models here.

class enquiryAdmin(admin.ModelAdmin):
    class Meta:
        model=enquiry
        fields='__all__'

admin.site.register(enquiry,enquiryAdmin)
