from datetime import timedelta

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Avg, Count
from django.urls import reverse
from django.utils import timezone

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tags", args=[self.name])

    @staticmethod
    def most_used_tags():
        yesterday = timezone.now() - timedelta(days=1)
        Tags = (
            Tag.objects.filter(post__creation_datetime__gte=yesterday)
            .annotate(count=Count("post__id"))
            .order_by("-count")[:5]
        )
        return Tags


class Like(models.Model):
    post = models.ForeignKey(
        "posts.Post", related_name="likes", on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, related_name="likes", on_delete=models.CASCADE)


class Rate(models.Model):
    rating = models.IntegerField(default=1, choices=[(i, i) for i in [1, 2, 3, 4, 5]])
    post = models.ForeignKey(
        "posts.Post", on_delete=models.CASCADE, related_name="ratings"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.rating}"


class Post(models.Model):
    image = models.ImageField()
    text = models.TextField(max_length=2000)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_datetime = models.DateTimeField(auto_now_add=True)

    tags = models.ManyToManyField(Tag)
    likers = models.ManyToManyField(
        User, related_name="liked_posts", through="posts.Like"
    )
    rating = models.ManyToManyField(
        User, related_name="post_rating", through="posts.Rate"
    )

    def __str__(self):
        return f"{self.created_by} - {self.creation_datetime}"

    def get_absolute_url(self):
        return reverse("posts:update", args=[self.id])

    @property
    def average_rate(self):
        avg_rate = self.ratings.aggregate(average_rate=Avg("rating"))["average_rate"]
        return avg_rate or "0"
