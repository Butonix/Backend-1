# Generated by Django 3.1.3 on 2020-11-25 13:38

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0012_auto_20201125_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='contacts',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(unique=True), size=3),
        ),
    ]