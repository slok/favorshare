from django.db import models
from django.utils.translation import ugettext_lazy as _

from .fields import AutoDateTimeField


class AutoDateTimeModel(models.Model):
    created = models.DateTimeField(
        _("creation datetime"),
        auto_now_add=True
    )
    updated = AutoDateTimeField(
        _("last updated datetime"),
        null=True
    )

    class Meta:
        abstract = True
