from django.db import models
import datetime
from django.utils import timezone
import recruitment.settings as settings
from django.core.files.storage import FileSystemStorage   

STATUSES = (
    ('pending','PENDING'),
    ('rejected','REJECTED'),
    ('approved','APPROVED'),
)

class Applicant(models.Model):
    full_name = models.CharField(max_length=200,verbose_name='Full Name')
    email = models.CharField(max_length=300)
    status = models.CharField(max_length=10,default='pending',choices=STATUSES)
    interests = models.CharField(max_length=1000,default='-')
    visits = models.IntegerField(default=0)
    applied_date = models.DateTimeField(auto_now_add=True)
    cv = models.FileField(
        # upload_to=settings.CV_ROOT,
        upload_to=settings.CV_DIRNAME,
        storage=FileSystemStorage(
            location=settings.MEDIA_ROOT,
            base_url=settings.MEDIA_URL,
            # base_url=settings.CV_URL,
        )
    )

    def __str__(self):
        return self.full_name


    # was_published_recently.admin_order_field = 'pub_date'
    # was_published_recently.boolean = True
    # was_published_recently.short_description = 'Published recently?'
