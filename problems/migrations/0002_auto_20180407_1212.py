# Generated by Django 2.0.1 on 2018-04-07 06:12

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lemma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='de')),
            ],
        ),
        migrations.AddField(
            model_name='problem',
            name='hashtags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=[''], size=None),
        ),
    ]
