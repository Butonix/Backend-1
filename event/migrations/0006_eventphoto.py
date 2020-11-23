# Generated by Django 3.1.3 on 2020-11-23 16:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_event_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='event/photos', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff'])])),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BaseEvent', to='event.event')),
            ],
        ),
    ]