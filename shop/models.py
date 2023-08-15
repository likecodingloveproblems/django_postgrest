from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from shop.querysets import ProductQuerySet
from utils.models import Archivable


class Shop(Archivable, models.Model):
    name = models.CharField(_("name"), max_length=127)
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("manager"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Shop")
        verbose_name_plural = _("Shops")

    def __str__(self):
        return self.name


class Product(Archivable, models.Model):
    name = models.CharField(_("product"), max_length=127)
    description = models.TextField(_("description"))
    shop = models.ForeignKey(Shop, verbose_name=_("shop"), on_delete=models.CASCADE)
    price = models.FloatField(_("price"))
    discount = models.FloatField(_("discount"))
    inventory = models.IntegerField(_("inventory"))

    objects = ProductQuerySet.as_manager()

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name
