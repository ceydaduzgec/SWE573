# Generated by Django 3.2.13 on 2022-12-19 21:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='follower_users', to=settings.AUTH_USER_MODEL, verbose_name='Followers'),
        ),
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='following_users', to=settings.AUTH_USER_MODEL, verbose_name='Following'),
        ),
    ]