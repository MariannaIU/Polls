# Generated by Django 4.0 on 2022-01-15 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='description',
            field=models.CharField(blank=True, max_length=4000, null=True),
        ),
        migrations.AddField(
            model_name='poll',
            name='finish',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='poll',
            name='start',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
