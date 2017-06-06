from django.contrib import admin

from .models import Applicant

class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'interests','cv','status')
    list_filter = ['status']
    search_fields = ['full_name','email','interests']
    # readonly_fields = ['cv'] #,'visits']
    readonly_fields = ['cv'] #,'visits']
    exclude = ['visits']


admin.site.register(Applicant, ApplicantAdmin)

