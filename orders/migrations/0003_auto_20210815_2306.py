# Generated by Django 3.2.5 on 2021-08-16 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
    ]