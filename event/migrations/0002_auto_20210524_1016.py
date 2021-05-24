# Generated by Django 3.1.8 on 2021-05-24 04:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='is_approved',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='is_main',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='eventinterest',
            name='attended',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='eventinterest',
            name='event',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='interested_event', to='event.event'),
        ),
        migrations.AlterField(
            model_name='eventinterest',
            name='follower',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='interested_followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='eventinterest',
            name='going',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='eventinterest',
            name='interested',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]