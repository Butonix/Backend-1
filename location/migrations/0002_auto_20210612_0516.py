# Generated by Django 3.1.8 on 2021-06-11 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vdc',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]