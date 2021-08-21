from django.contrib.auth import get_user_model
from django.db import models

from utils.constants import MULTIMEDIA_TYPE


class Multimedia(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.CharField(blank=True, null=True, max_length=2048)
    is_pinned = models.BooleanField(default=False, editable=False)
    type = models.CharField(choices=MULTIMEDIA_TYPE, default='satsang', max_length=11)
    pinner = models.ForeignKey(
        get_user_model(),
        on_delete=models.DO_NOTHING,
        related_name="pinned_multimedias",
        null=True,
        blank=True,
        editable=False,
    )
    is_approved = models.BooleanField(default=False, editable=False)
    approved_at = models.DateTimeField(
        default=None, null=True, blank=True, editable=False
    )
    approved_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.DO_NOTHING,
        related_name="approved_multimedias",
        null=True,
        blank=True,
        editable=False,
    )
    uploaded_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.DO_NOTHING,
        related_name="my_multimedias",
        editable=False,
    )
    timestamp = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-timestamp"]
