# Generated by Django 3.1.8 on 2021-06-12 19:04

import django.db.models.deletion
from django.db import migrations, models

import utilities.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_us', models.TextField(max_length=10000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'About Us',
                'verbose_name_plural': 'About Us',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=utilities.models.upload_services_images_to)),
                ('title', models.CharField(max_length=16)),
                ('description', models.TextField(max_length=1024)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Services',
                'verbose_name_plural': 'Services',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ShowcaseGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=utilities.models.upload_showcase_gallery_image_to)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Showcase Gallery',
                'verbose_name_plural': 'Showcase Gallery',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=utilities.models.upload_showcase_slider_image_to)),
                ('title', models.TextField(blank=True, max_length=512, null=True)),
                ('context', models.TextField(blank=True, max_length=512, null=True)),
                ('subtitle', models.TextField(blank=True, max_length=1024, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Showcase Slider',
                'verbose_name_plural': 'Showcase Slider',
            },
        ),
        migrations.CreateModel(
            name='AboutUsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=utilities.models.upload_about_us_images_to)),
                ('about_us', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='about_us_images', to='utilities.aboutus')),
            ],
            options={
                'verbose_name': 'About Us Image',
                'verbose_name_plural': 'About Us Images',
            },
        ),
    ]
