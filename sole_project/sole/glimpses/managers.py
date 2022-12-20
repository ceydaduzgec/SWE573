from django.db.models import Manager, QuerySet


class GlimpseQuerySet(QuerySet):
    @property
    def allowed_glimpses(self):
        return self.all()


class GlimpseManager(Manager):
    def get_queryset(self):
        return GlimpseQuerySet(self.model, using=self._db)

    @property
    def allowed_glimpses(self):
        return self.get_queryset().allowed_glimpses
