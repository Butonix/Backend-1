# Generated by Django 3.1.3 on 2020-11-28 14:20

from django.conf import settings
import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('slogan', models.TextField(blank=True, max_length=512, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='branch', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff', 'JPG'])])),
                ('contacts', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveBigIntegerField(unique=True), size=3)),
                ('is_main', models.BooleanField(default=False, verbose_name='Is Main Branch')),
                ('is_approved', models.BooleanField(default=False)),
                ('approved_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('approved_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='BranchApprover', to=settings.AUTH_USER_MODEL)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='BranchCountry', to='location.country')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Creator', to=settings.AUTH_USER_MODEL)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='BranchDistrict', to='location.district')),
                ('municipality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='BranchMunicipality', to='location.municipality')),
                ('municipality_ward', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='BranchMunicipalityWardNumber', to='location.municipalityward')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='BranchProvince', to='location.province')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Modifier', to=settings.AUTH_USER_MODEL)),
                ('vdc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='BranchVdc', to='location.vdc')),
                ('vdc_ward', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='BranchVdcWardNumber', to='location.vdcward')),
            ],
            options={
                'verbose_name_plural': 'Branches',
            },
        ),
    ]
