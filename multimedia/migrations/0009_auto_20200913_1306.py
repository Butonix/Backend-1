# Generated by Django 3.1.1 on 2020-09-13 07:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('multimedia', '0008_auto_20200913_1301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='love',
            old_name='isLoved',
            new_name='is_loved',
        ),
    ]
