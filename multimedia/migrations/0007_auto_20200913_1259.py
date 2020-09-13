# Generated by Django 3.1.1 on 2020-09-13 07:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('multimedia', '0006_auto_20200913_1242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ArticleComment', to='multimedia.article')),
                ('multimedia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='MultimediaComment', to='multimedia.multimedia')),
                ('reply_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CommentReplies', to='multimedia.comment')),
                ('writer', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='CommentWriter', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Comments',
                'unique_together': {('article', 'writer'), ('multimedia', 'writer')},
            },
        ),
        migrations.CreateModel(
            name='Love',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isLoved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='LoveArticle', to='multimedia.article')),
                ('lover', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='MediaLover', to=settings.AUTH_USER_MODEL)),
                ('multimedia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='LoveMultimedia', to='multimedia.multimedia')),
            ],
            options={
                'unique_together': {('article', 'lover'), ('multimedia', 'lover')},
            },
        ),
        migrations.DeleteModel(
            name='MediaComment',
        ),
    ]