# Generated by Django 4.0 on 2022-01-31 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_poll_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='total',
        ),
    ]
