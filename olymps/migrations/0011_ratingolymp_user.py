# Generated by Django 2.0.1 on 2018-04-22 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20180411_1849'),
        ('olymps', '0010_remove_ratingolymp_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratingolymp',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='accounts.Profile'),
            preserve_default=False,
        ),
    ]
