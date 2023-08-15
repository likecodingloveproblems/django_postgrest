from django.db.models import QuerySet


class ProductQuerySet(QuerySet):
    def available(self):
        return self.filter(is_archived=False)

    def for_shop(self, shop):
        return self.filter(shop=shop)
