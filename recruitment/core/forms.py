from django import forms
from django.core.exceptions import ValidationError
from recruitment.core.models import Applicant

def validate_file_extension(value):
    if value.content_type != 'application/pdf':
        raise ValidationError(u'File Type Not Allowed')
    return True

class ApplicantForm(forms.ModelForm):

    class Meta:
        model = Applicant
        fields = [
            'full_name',
            'email',
            'cv',
            'interests']

    def __init__(self,*args,**kwargs):
        super(ApplicantForm,self).__init__(*args,**kwargs)
        self.fields['cv'].widget.attrs['accept'] = '.pdf,.doc,.docx'


            
