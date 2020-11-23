# Generated by Django 3.1.3 on 2020-11-23 17:31

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0009_auto_20201123_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventvideourls',
            name='video_urls',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(unique=True), size=10),
        ),
    ]