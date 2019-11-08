# Generated by Django 2.2.6 on 2019-10-29 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, verbose_name='вопрос')),
                ('description', models.TextField(verbose_name='подробности вопроса')),
                ('answers_count', models.IntegerField(default=0, verbose_name='ответы')),
                ('rating', models.IntegerField(default=0, verbose_name='рейтинг')),
                ('creation_time', models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания')),
                ('published', models.BooleanField(default=True, verbose_name='опубликован?')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='имя')),
                ('birthday', models.DateField(verbose_name='дата рождения')),
                ('about', models.TextField(default='Пользователь не рассказал о себе.', verbose_name='о пользователе')),
                ('avatar', models.FileField(upload_to='upload/')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=20, verbose_name='тег')),
                ('questions_count', models.IntegerField(default=0, verbose_name='ответы')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Users', verbose_name='добавил тег')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='QuestTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Questions', verbose_name='вопрос')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Tags', verbose_name='тег')),
            ],
        ),
        migrations.AddField(
            model_name='questions',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Users', verbose_name='автор'),
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(verbose_name='текст ответа')),
                ('creation_time', models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Users', verbose_name='автор')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Questions', verbose_name='вопрос')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]
