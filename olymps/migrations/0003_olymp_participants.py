# Generated by Django 2.0.1 on 2018-04-14 20:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('olymps', '0002_ratingolymp'),
    ]

    operations = [
        migrations.AddField(
            model_name='olymp',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='olymp_participants', to=settings.AUTH_USER_MODEL),
        ),
    ]
