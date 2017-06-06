from django.shortcuts import render
# from django.http import HttpResponseRedirect
from .forms import ApplicantForm
import recruitment.settings as settings

def upload_file(request):
    if request.method == 'POST':
        form = ApplicantForm(request.POST, request.FILES)
        
        if form.is_valid():
            applicant = form.save()
            file_path = settings.MEDIA_URL + applicant.cv.name
            return render(request, 'home.html', {
                'form': form,
                'uploaded_file_url':file_path,
                })
        else:
            print ('invalid form')
    else:
        form = ApplicantForm()
    return render(request, 'home.html', {'form': form})

index = upload_file

# https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html
# https://docs.djangoproject.com/en/1.11/topics/http/file-uploads/

# https://docs.djangoproject.com/en/1.7/topics/templates/
# https://tutorial.djangogirls.org/en/template_extending/
