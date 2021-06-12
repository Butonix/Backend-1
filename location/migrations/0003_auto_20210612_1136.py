# Generated by Django 3.1.8 on 2021-06-12 05:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20210612_0516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='municipality',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='municipalityward',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='municipalityward',
            name='number',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(60), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='vdcward',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='vdcward',
            name='number',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(60), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterUniqueTogether(
            name='municipality',
            unique_together={('name', 'district')},
        ),
        migrations.AlterUniqueTogether(
            name='municipalityward',
            unique_together={('name', 'municipality', 'number')},
        ),
        migrations.AlterUniqueTogether(
            name='vdc',
            unique_together={('name', 'district')},
        ),
        migrations.AlterUniqueTogether(
            name='vdcward',
            unique_together={('name', 'vdc', 'number')},
        ),
    ]
