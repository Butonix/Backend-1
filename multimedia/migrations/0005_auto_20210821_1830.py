# Generated by Django 3.1.8 on 2021-08-21 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multimedia', '0004_multimedia_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multimedia',
            name='type',
            field=models.CharField(choices=[('satsang', 'Satsang'), ('prayer', 'Prayer'), ('testimonial', 'Testimonial'), ('bhajan', 'Bhajan'), ('bachan', 'Bachan')], default='satsang', max_length=11),
        ),
    ]
