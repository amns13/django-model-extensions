from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CreateUpdateTimestampManager(models.Manager):
    """
    Custom Manager for CreatedUpdatedTimestampModel.
    Used to update last_update_at on update.
    """

    def update(self, **kwargs: any) -> int:
        """
        Update values of fields in kwargs along with last_updated_at field.

        Returns:
            int: Number of records updated.
        """
        kwargs["last_updated_at"] = timezone.now()
        return super().update(**kwargs)


class CreatedUpdatedTimestampModel(models.Model):
    """
    An abstract base class that provides self-managed "created_at" and
    "last_updated_at" fields.
    """

    created_at = models.DateTimeField(_("created timestamp"), auto_now_add=True)
    last_updated_at = models.DateTimeField(_("last update timestamp"), auto_now=True)

    objects = CreateUpdateTimestampManager()

    class Meta:
        abstract = True
        get_latest_by = "last_updated_at"
