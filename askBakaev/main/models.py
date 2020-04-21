from django.db import models
from datetime import datetime
import django.utils.timezone as tz


# class Users(models.Model):
#     name = models.CharField(max_length=20, verbose_name="имя")
#     birthday = models.DateField(verbose_name='дата рождения')
#     about = models.TextField(default="Пользователь не рассказал о себе.", verbose_name="о пользователе")
#     avatar = models.ImageField(upload_to='upload/')
#     password = models.CharField(default="qwertyqwerty", max_length=32, verbose_name="parol'")
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = "Пользователь"
#         verbose_name_plural = "Пользователи"
#
#
# class QuestManager(models.Manager):
#     def increment(self, question):
#         print("increment is called")
#         # return
#
#
# class Questions(models.Model):
#     question = models.CharField(max_length=200, verbose_name="вопрос")
#     description = models.TextField(verbose_name="подробности вопроса")
#     author = models.ForeignKey(
#         Users, on_delete=models.CASCADE, related_name='user', verbose_name="автор")
#     answers_count = models.IntegerField(default=0, verbose_name="ответы")
#     rating = models.IntegerField(default=0, verbose_name="рейтинг")
#     views = models.IntegerField(default=0, verbose_name="просмотры")
#     creation_time = models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания')
#     published = models.BooleanField(default=True, verbose_name="опубликован?")
#     tags = models.ManyToManyField('Tags', blank=True, related_name='tags', verbose_name='Теги')
#
#     def __str__(self):
#         return self.question
#
#     objects = QuestManager()
#
#     class Meta:
#         verbose_name = "Вопрос"
#         verbose_name_plural = "Вопросы"
#
#
# class Answers(models.Model):
#     answer = models.TextField(verbose_name="текст ответа")
#     question = models.ForeignKey(
#         Questions, on_delete=models.CASCADE, verbose_name="вопрос")
#     author = models.ForeignKey(
#         Users, on_delete=models.CASCADE, related_name='answers', verbose_name="автор")
#     creation_time = models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания')
#     right_answer = models.BooleanField(default=False, verbose_name="верный ответ")
#
#     def __str__(self):
#         return "{} -> {}".format(self.answer, self.question)
#
#     class Meta:
#         verbose_name = "Ответ"
#         verbose_name_plural = "Ответы"
#
#
# class Tags(models.Model):
#     tag = models.CharField(max_length=20, verbose_name="тег")
#     author = models.ForeignKey(
#         Users, on_delete=models.CASCADE, verbose_name="добавил тег")
#     questions_count = models.IntegerField(default=0, verbose_name="вопросы")
#
#     def __str__(self):
#         return self.tag
#
#     class Meta:
#         verbose_name = "Тег"
#         verbose_name_plural = "Теги"


class Rewiews(models.Model):
    author_nick = models.CharField(u'Автор', default="Имя не указано.", max_length=255)
    text = models.TextField(u'Текст', default="Текст не указан.")
    creation_date = models.DateTimeField(u'Дата создания', default=tz.now())
    seen = models.BooleanField(default=False, verbose_name="Виден?")

    def __str__(self):
        return "{} : {}".format(self.author_nick, self.text)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class Messages(models.Model):
    email = models.CharField(u'Почта', default="Эмейл не указан.", max_length=255)
    number = models.CharField(u'Номер', default="Номер не указан.", max_length=30)
    JURY = 'JR'
    PHYSIC = 'PH'
    YEAR_IN_SCHOOL_CHOICES = [
        (JURY, 'Для юридических лиц'),
        (PHYSIC, 'Для физических лиц'),
    ]
    usluga = models.CharField(
        u'Услуга',
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=PHYSIC,
    )
    text = models.TextField(u'Проблема', default="Текст проблемы пуст.")
    creation_date = models.DateTimeField(u'Дата создания', default=tz.now())
    seen = models.BooleanField(default=False, verbose_name="Виден?")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
