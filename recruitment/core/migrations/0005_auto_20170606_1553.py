# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 12:53
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20170606_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='cv',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(base_url='/media/', location='/home/rawad/projects/recruitment_project/recruitment/media'), upload_to='CVs'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='status',
            field=models.CharField(choices=[('pending', 'PENDING'), ('rejected', 'REJECTED'), ('approved', 'APPROVED')], default='pending', max_length=10),
        ),
    ]
