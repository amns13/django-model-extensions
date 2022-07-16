from typing import Any, Collection, Iterable, Optional, Sequence

from django.conf import settings
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
        """
        kwargs["last_updated_at"] = timezone.now()
        return super().update(**kwargs)

    def bulk_update(
        self,
        objs: Iterable["CreatedUpdatedTimestampModel"],
        fields: Sequence[str],
        batch_size: Optional[int] = None,
    ) -> int:
        """
        Overriden bulk_update method. Adds current timestamp to last_updated_at field.
        """
        timestamp = timezone.now()
        for obj in objs:
            obj.last_updated_at = timestamp
        fields.append("last_updated_at")
        return super().bulk_update(objs, fields, batch_size)


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


class CreatedUpdatedByModel(models.Model):
    """
    An abstract base class that provides "created_by" and
    "last_updated_by" fields.
    These fields are not self managed and need to be handled
    by the user of this model.
    By default, these fields are None.
    """

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)ss_created",
        related_query_name="%(app_label)s_%(class)s_created",
        null=True,
        blank=True,
        verbose_name=_("created by"),
        editable=False,
    )
    last_updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)ss_last_updated",
        related_query_name="%(app_label)s_%(class)s_last_updated",
        null=True,
        blank=True,
        verbose_name=_("last updated by"),
        editable=False,
    )

    class Meta:
        abstract = True

    @classmethod
    def from_db(
        cls, db: Optional[str], field_names: Collection[str], values: Collection[Any]
    ) -> "CreatedUpdatedByModel":
        instance = super().from_db(db, field_names, values)
        instance._old_values = dict(zip(field_names, values))
        return instance

    def save(self, *args, **kwargs) -> None:
        if self.pk:
            self.created_by_id = self._old_values["created_by_id"]
        return super().save(*args, **kwargs)


class CreatedUpdatedTimeUserModel(CreatedUpdatedTimestampModel, CreatedUpdatedByModel):
    """
    An abstract base class that provides "created_at", "last_updated_at",
    "created_by", and "last_updated_by" fields.
    "created_at", "last_updated_at" are self-managed fields.
    "created_by", and "last_updated_by" are not self-managed and need to be handled
    by the user of the model.
    """

    class Meta(CreatedUpdatedTimestampModel.Meta):
        # Inherited from CreatedUpdatedTimestampModel.Meta for get_latest_by attribute
        abstract = True
