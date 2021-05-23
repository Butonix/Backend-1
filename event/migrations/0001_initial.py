# Generated by Django 3.1.8 on 2021-05-13 19:14

import django.core.validators
import django.db.models.deletion
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("branch", "0001_initial"),
        ("location", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=64, unique=True)),
                (
                    "description",
                    models.TextField(blank=True, max_length=512, null=True),
                ),
                ("venue", models.CharField(max_length=64)),
                ("start_date", models.DateField()),
                ("duration", models.IntegerField()),
                (
                    "time_of_day",
                    models.CharField(
                        choices=[
                            ("Morning", "Morning"),
                            ("Afternoon", "Afternoon"),
                            ("Evening", "Evening"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Satsang", "Satsang"),
                            ("General Meeting", "General Meeting"),
                            ("Board Meeting", "Board Meeting"),
                        ],
                        max_length=15,
                    ),
                ),
                ("is_approved", models.BooleanField(default=False)),
                ("is_main", models.BooleanField(default=False)),
                (
                    "banner",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="events",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                ["png", "jpg", "jpeg", "gif", "bmp", "tiff", "JPG"]
                            )
                        ],
                    ),
                ),
                (
                    "contact",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None, unique=True
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "approved_at",
                    models.DateTimeField(blank=True, editable=False, null=True),
                ),
                (
                    "approved_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="EventApprover",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="EventCountry",
                        to="location.country",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="EventCreator",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "district",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="EventDistrict",
                        to="location.district",
                    ),
                ),
                (
                    "municipality",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="EventMunicipality",
                        to="location.municipality",
                    ),
                ),
                (
                    "municipality_ward",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="EventMunicipalityWardNumber",
                        to="location.municipalityward",
                    ),
                ),
                (
                    "organizer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="EventOrganizer",
                        to="branch.branch",
                    ),
                ),
                (
                    "province",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="EventProvince",
                        to="location.province",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="EventModifier",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "vdc",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="EventVdc",
                        to="location.vdc",
                    ),
                ),
                (
                    "vdc_ward",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="EventVdcWardNumber",
                        to="location.vdcward",
                    ),
                ),
            ],
            options={
                "permissions": [
                    ("approve_event", "Can toggle approval status of event")
                ],
            },
        ),
        migrations.CreateModel(
            name="EventVideoUrl",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("video_url", models.URLField(unique=True)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="video_urls",
                        to="event.event",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EventPhoto",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="event/photos",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                ["png", "jpg", "jpeg", "gif", "bmp", "tiff", "JPG"]
                            )
                        ],
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="BaseEvent",
                        to="event.event",
                    ),
                ),
            ],
        ),
    ]
