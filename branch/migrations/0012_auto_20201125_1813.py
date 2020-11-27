# Generated by Django 3.1.3 on 2020-11-25 12:28

import django.contrib.postgres.fields
import django.db.models.deletion
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('branch', '0011_auto_20201123_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='phone',
        ),
        migrations.AddField(
            model_name='branch',
            name='approved_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='branch',
            name='approved_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='BranchApprover', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='branch',
            name='contacts',
            field=django.contrib.postgres.fields.ArrayField(base_field=phonenumber_field.modelfields.PhoneNumberField(max_length=15, region=None, unique=True), default=['9856252525'], size=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branch',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]