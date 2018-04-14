# Generated by Django 2.0.1 on 2018-04-14 20:36

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('olymps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingOlymp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None), default=[['first', ' ']], size=None)),
                ('olymp', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='olymps.Olymp')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
