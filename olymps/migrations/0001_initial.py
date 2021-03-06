# Generated by Django 2.0.1 on 2018-05-01 23:30

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import olymps.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0007_auto_20180411_1849'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Olymp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField(unique=True)),
                ('draft', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=olymps.models.upload_location, width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('publish', models.DateField()),
                ('start_time', models.DateField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('participants', models.ManyToManyField(blank=True, related_name='olymp_participants', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['start_time', '-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='RatingOlymp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None), default=[['Summary', '0']], size=None)),
                ('summary', models.IntegerField(default=0)),
                ('olymp', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='olymps.Olymp')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.Profile')),
            ],
            options={
                'ordering': ['-summary'],
            },
        ),
    ]
