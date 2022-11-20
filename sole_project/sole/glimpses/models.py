from datetime import timedelta

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Avg, Count
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.utils import timezone

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(_("Name"), max_length=20, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tags", args=[self.name])

    @staticmethod
    def most_used_tags():
        yesterday = timezone.now() - timedelta(days=1)
        Tags = (
            Tag.objects.filter(glimpse__creation_datetime__gte=yesterday)
            .annotate(count=Count("glimpse__id"))
            .order_by("-count")[:5]
        )
        return Tags


class Like(models.Model):
    glimpse = models.ForeignKey("glimpses.Glimpse", related_name="likes", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="likes", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.glimpse}"

class Rating(models.Model):
    glimpse = models.ForeignKey("glimpses.Glimpse", related_name="ratings", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="ratings", on_delete=models.CASCADE)

    rating = models.IntegerField(_("Rating"), default=1, choices=[(i, i) for i in [1, 2, 3, 4, 5]])

    def __str__(self):
        return f"{self.rating}"


class Comment(models.Model):
    glimpse = models.ForeignKey("glimpses.Glimpse", related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name="comments", on_delete=models.CASCADE)

    comment = models.IntegerField(_("Comment"))

    def __str__(self):
        return f"{self.rating}"


class Glimpse(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'draft', _('Draft')
        PUBLIC = 'public', _('Public')
        PRIVATE = 'private', _('Private')

    title = models.CharField(_('Title'), max_length=255)
    text = models.TextField(_("Text"), max_length=2000, blank=True)
    url = models.URLField(_("URL"), max_length=255,blank=True)
    status = models.CharField(_("Status"), max_length=255, choices=Status.choices)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_datetime = models.DateTimeField(_("Created on"), auto_now_add=True)

    tags = models.ManyToManyField(Tag, verbose_name=_('Tags'), blank=True)
    liked_by = models.ManyToManyField(User, related_name="liked_glimpses", through="glimpses.Like", verbose_name=_('Likes'))
    ratings = models.ManyToManyField(User, related_name="ratingd_glimpses", through="glimpses.Rating", verbose_name=_('Ratings'))
    comments = models.ManyToManyField(User, related_name="commented_glimpses", through="glimpses.Comment", verbose_name=_('Comments'))

    def __str__(self):
        return f"{self.created_by} - {self.creation_datetime}"

    def get_absolute_url(self):
        return reverse("glimpses:update", args=[self.id])

    @property
    def average_rating(self):
        avg_rating = self.ratings.aggregate(average_rating=Avg("rating"))["average_rating"]
        return avg_rating or "0"
