# Generated by Django 3.1.1 on 2020-09-12 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
        ('branch', '0004_auto_20200907_1614'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branch',
            options={'verbose_name_plural': 'Branches'},
        ),
        migrations.AlterField(
            model_name='branch',
            name='municipality_ward_no',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='BranchMunicipalityWardNo', to='location.municipalitywardnumber', unique=True),
        ),
        migrations.AlterField(
            model_name='branch',
            name='vdc_ward_no',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='BranchVdcWardNo', to='location.vdcwardnumber', unique=True),
        ),
    ]