# Generated by Django 2.2.12 on 2020-04-20 22:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20200420_2159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='Эмейл не указан.', max_length=255, verbose_name='Почта')),
                ('number', models.TextField(default='Номер не указан.', verbose_name='Номер')),
                ('usluga', models.CharField(choices=[('JR', 'Для юридических лиц'), ('PH', 'Для физических лиц')], default='PH', max_length=2)),
                ('text', models.TextField(default='Текст проблемы пуст.', verbose_name='Проблема')),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2020, 4, 20, 22, 11, 11, 97677, tzinfo=utc), verbose_name='Дата создания')),
                ('seen', models.BooleanField(default=False, verbose_name='Виден?')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.AlterField(
            model_name='rewiews',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 20, 22, 11, 11, 97254, tzinfo=utc), verbose_name='Дата создания'),
        ),
    ]