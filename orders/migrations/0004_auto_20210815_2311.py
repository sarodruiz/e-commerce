# Generated by Django 3.2.5 on 2021-08-16 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20210815_2306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='first',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last',
        ),
    ]
