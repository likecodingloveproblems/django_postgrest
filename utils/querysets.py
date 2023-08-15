from django.db.models import QuerySet


class ArchivableQuerySet(QuerySet):
    def available(self):
        return self.filter(is_archived=False)
