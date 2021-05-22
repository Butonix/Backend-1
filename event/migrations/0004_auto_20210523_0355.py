# Generated by Django 3.1.8 on 2021-05-22 22:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('branch', '0002_auto_20210522_1901'),
        ('location', '0001_initial'),
        ('event', '0003_auto_20210523_0346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='approved_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='events_approved', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='country_events', to='location.country'),
        ),
        migrations.AlterField(
            model_name='event',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='events_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(max_length=512, unique=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='district_events', to='location.district'),
        ),
        migrations.AlterField(
            model_name='event',
            name='municipality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='municipality_events', to='location.municipality'),
        ),
        migrations.AlterField(
            model_name='event',
            name='municipality_ward',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='municipality_ward_events', to='location.municipalityward'),
        ),
        migrations.AlterField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branch_events', to='branch.branch'),
        ),
        migrations.AlterField(
            model_name='event',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='province_events', to='location.province'),
        ),
        migrations.AlterField(
            model_name='event',
            name='updated_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='events_updated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='vdc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='vdc_events', to='location.vdc'),
        ),
        migrations.AlterField(
            model_name='event',
            name='vdc_ward',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='vdc_ward_events', to='location.vdcward'),
        ),
    ]
