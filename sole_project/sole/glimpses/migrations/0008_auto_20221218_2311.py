# Generated by Django 3.2.13 on 2022-12-18 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('glimpses', '0007_auto_20221130_0023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='glimpse',
            name='ratings',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
