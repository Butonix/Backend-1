# Generated by Django 3.1.8 on 2021-06-01 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("branch", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="branchimage",
            name="timestamp",
            field=models.DateTimeField(auto_now=True),
        ),
    ]