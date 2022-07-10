from django.db import models
from django.utils.translation import gettext_lazy as _


class CreatedUpdatedTimestampModel(models.Model):
    """
    An abstract base class that provides self-managed "created_at" and
    "last_updated_at" fields.
    """

    created_at = models.DateTimeField(_("created timestamp"), auto_now_add=True)
    last_updated_at = models.DateTimeField(_("last update timestamp"), auto_now=True)

    class Meta:
        abstract = True
        get_latest_by = "last_updated_at"
