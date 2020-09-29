# Generated by Django 3.1.1 on 2020-09-19 06:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0009_auto_20200913_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='image',
            field=models.ImageField(default='default/member.png', upload_to='branch', validators=[
                django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff'])]),
        ),
    ]
