# Generated by Django 3.1.5 on 2021-01-24 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('praying', '0009_auto_20210123_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='pray_tb',
            name='daily_prayer_detail',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='more_tb',
        ),
    ]
