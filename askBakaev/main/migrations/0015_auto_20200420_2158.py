# Generated by Django 2.2.12 on 2020-04-20 21:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20200420_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rewiews',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 20, 21, 58, 24, 426156), verbose_name='Дата создания'),
        ),
    ]