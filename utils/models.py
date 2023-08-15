from django.db import models
from django.utils.translation import gettext_lazy as _


class Archivable(models.Model):
    is_archived = models.BooleanField(_("is archived?"), default=False)

    class Meta:
        abstract = True
        verbose_name = _("Archivable")
        verbose_name_plural = _("Archivables")
