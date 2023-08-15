from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.querysets import ArchivableQuerySet


class Archivable(models.Model):
    is_archived = models.BooleanField(_("is archived?"), default=False)

    objects = ArchivableQuerySet.as_manager()

    class Meta:
        abstract = True
        verbose_name = _("Archivable")
        verbose_name_plural = _("Archivables")
