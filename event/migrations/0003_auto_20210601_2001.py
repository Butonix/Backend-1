# Generated by Django 3.1.8 on 2021-06-01 14:16

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_eventbannerimage_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='contact',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
