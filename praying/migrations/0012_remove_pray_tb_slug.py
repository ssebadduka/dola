# Generated by Django 3.1.5 on 2021-01-25 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('praying', '0011_pray_tb_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pray_tb',
            name='slug',
        ),
    ]
