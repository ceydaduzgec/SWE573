# Generated by Django 3.2.13 on 2022-12-19 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glimpses', '0010_auto_20221219_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=128, unique=True, verbose_name='Name'),
        ),
    ]
