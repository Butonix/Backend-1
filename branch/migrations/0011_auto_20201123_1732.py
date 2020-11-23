# Generated by Django 3.1.3 on 2020-11-23 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0010_branch_slogan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='branch',
            name='slogan',
            field=models.TextField(blank=True, max_length=512, null=True),
        ),
    ]
