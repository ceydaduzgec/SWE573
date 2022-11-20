# Generated by Django 3.2.13 on 2022-11-20 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glimpses', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='glimpse',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('public', 'Public'), ('private', 'Private')], default='draft', max_length=255, verbose_name='Status'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='glimpse',
            name='tags',
            field=models.ManyToManyField(blank=True, to='glimpses.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='glimpse',
            name='text',
            field=models.TextField(blank=True, max_length=2000, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='glimpse',
            name='url',
            field=models.URLField(blank=True, max_length=255, verbose_name='URL'),
        ),
    ]