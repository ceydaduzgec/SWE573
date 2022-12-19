from datetime import timedelta

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Count
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(_("Name"), max_length=128, unique=True)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tags", args=[self.name])

    @staticmethod
    def most_used_tags():
        yesterday = timezone.now() - timedelta(days=1)
        tags = (
            Tag.objects.filter(glimpse__creation_datetime__gte=yesterday)
            .annotate(count=Count("glimpse__id"))
            .order_by("-count")[:5]
        )
        return tags


class Like(models.Model):
    glimpse = models.ForeignKey("glimpses.Glimpse", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="likes", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.glimpse}"


class Comment(models.Model):
    glimpse = models.ForeignKey("glimpses.Glimpse", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    comment = models.TextField(_("Comment"), max_length=2000, blank=True, null=False)
    creation_datetime = models.DateTimeField(_("Created on"), auto_now_add=True)

    def __str__(self):
        return f"{self.comment}"


class Space(models.Model):
    title = models.CharField(_("Title on"), max_length=255, unique=False)
    description = models.CharField(_("Description"), max_length=255, blank=True, unique=False)
    creation_datetime = models.DateTimeField(_("Created on"), auto_now_add=True)
    update_datetime = models.DateTimeField(_("Updated on"), auto_now=True)
    owner = models.ForeignKey(User, related_name="owner", on_delete=models.CASCADE, verbose_name=_("Owner"))
    members = models.ManyToManyField(User, related_name="members", verbose_name=_("Members"))

    def __str__(self):
        return self.title


class Glimpse(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", _("Draft")
        PUBLIC = "public", _("Public")
        PRIVATE = "private", _("Private")

    class Category(models.TextChoices):
        VIDEO = "video", _("Video")
        AUDIO = "audio", _("Audio")
        IMAGE = "image", _("Image")
        READING = "reading", _("Reading")
        EVENT = "event", _("Event")
        PLACE = "place", _("Place")
        APP = "app", _("Application")
        OTHER = "other", _("Other")

    title = models.CharField(_("Title"), max_length=50)
    description = models.TextField(_("Description"), max_length=255, blank=True, null=False)
    url = models.URLField(_("URL"), max_length=255, blank=True)
    status = models.CharField(_("Status"), max_length=255, choices=Status.choices)
    category = models.CharField(_("Category"), max_length=255, choices=Category.choices)

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Author"))
    creation_datetime = models.DateTimeField(_("Created on"), auto_now_add=True)
    update_datetime = models.DateTimeField(_("Updated on"), auto_now=True)

    tags = models.ManyToManyField(Tag, verbose_name=_("Tags"), blank=True)
    liked_by = models.ManyToManyField(
        User, related_name="liked_glimpses", through="glimpses.Like", verbose_name=_("Likes")
    )
    comments = models.ManyToManyField(
        User, related_name="commented_glimpses", through="glimpses.Comment", verbose_name=_("Comments")
    )

    def __str__(self):
        return f"{self.author} - {self.creation_datetime}"

    def get_absolute_url(self):
        return reverse("glimpses:update", args=[self.id])
