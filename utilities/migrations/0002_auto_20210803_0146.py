# Generated by Django 3.1.8 on 2021-08-02 20:01

import django.core.validators
from django.db import migrations, models
import utilities.models


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackfile',
            name='file',
            field=models.FileField(help_text='File to upload with feedback. Can be image, video, pdf, documents or zip files.', unique=True, upload_to=utilities.models.upload_feedback_file_to, validators=[django.core.validators.FileExtensionValidator(['webm', 'mp4', 'mpeg', 'flv', 'mov', 'MOV', 'png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff', 'JPG', 'pdf', 'docx', 'txt', 'zip'])]),
        ),
    ]
