from django.db.models import QuerySet

from utils.querysets import ArchivableQuerySet


class ProductQuerySet(ArchivableQuerySet, QuerySet):
    def for_shop(self, shop):
        return self.filter(shop=shop)
