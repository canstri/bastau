# Generated by Django 2.0.1 on 2018-04-16 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olymps', '0007_auto_20180417_0318'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ratingolymp',
            options={'ordering': ['-summary']},
        ),
        migrations.AddField(
            model_name='ratingolymp',
            name='summary',
            field=models.IntegerField(default=0),
        ),
    ]
