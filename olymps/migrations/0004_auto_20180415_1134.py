# Generated by Django 2.0.1 on 2018-04-15 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('olymps', '0003_olymp_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratingolymp',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.Profile'),
        ),
    ]