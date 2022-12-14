# Generated by Django 3.2.13 on 2022-12-18 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('glimpses', '0008_auto_20221218_2311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Space',
            fields=[
                ('id', models.BigIntegerField(editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Title on')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Description')),
                ('creation_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('update_datetime', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('members', models.ManyToManyField(related_name='members', to=settings.AUTH_USER_MODEL, verbose_name='Members')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='glimpse',
            name='text',
        ),
        migrations.AddField(
            model_name='glimpse',
            name='category',
            field=models.CharField(choices=[('video', 'Video'), ('audio', 'Audio'), ('image', 'Image'), ('event', 'Event'), ('place', 'Place'), ('app', 'Application')], default='', max_length=255, verbose_name='Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='glimpse',
            name='description',
            field=models.TextField(blank=True, max_length=255, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.BigIntegerField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='glimpse',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='glimpse',
            name='id',
            field=models.BigIntegerField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='like',
            name='id',
            field=models.BigIntegerField(editable=False, primary_key=True, serialize=False),
        ),
    ]
