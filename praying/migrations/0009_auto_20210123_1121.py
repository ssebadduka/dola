# Generated by Django 3.1.5 on 2021-01-23 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('praying', '0008_auto_20210123_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pray_tb',
            name='Book',
            field=models.CharField(max_length=45),
        ),
    ]