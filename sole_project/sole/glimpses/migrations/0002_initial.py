# Generated by Django 3.2.13 on 2022-11-20 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('glimpses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='like',
            name='glimpse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='glimpses.glimpse'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='glimpse',
            name='comment',
            field=models.ManyToManyField(related_name='commented_glimpses', through='glimpses.Comment', to=settings.AUTH_USER_MODEL, verbose_name='Comments'),
        ),
        migrations.AddField(
            model_name='glimpse',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='glimpse',
            name='liked_by',
            field=models.ManyToManyField(related_name='liked_glimpses', through='glimpses.Like', to=settings.AUTH_USER_MODEL, verbose_name='Likes'),
        ),
        migrations.AddField(
            model_name='glimpse',
            name='rating',
            field=models.ManyToManyField(related_name='ratingd_glimpses', through='glimpses.Rating', to=settings.AUTH_USER_MODEL, verbose_name='Ratings'),
        ),
        migrations.AddField(
            model_name='glimpse',
            name='tags',
            field=models.ManyToManyField(to='glimpses.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='comment',
            name='glimpse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='glimpses.glimpse'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
    ]