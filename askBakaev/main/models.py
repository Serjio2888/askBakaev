from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=20, verbose_name="имя")
    birthday = models.DateField(verbose_name='дата рождения')
    about = models.TextField(default="Пользователь не рассказал о себе.", verbose_name="о пользователе")
    avatar = models.ImageField(upload_to='upload/')
    password = models.CharField(default="qwertyqwerty", max_length=32, verbose_name="parol'")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

class QuestManager(models.Manager):
    def increment(self, question):
        print("increment is called")
        # return 

class Questions(models.Model):
    question = models.CharField(max_length=200, verbose_name = "вопрос")
    description = models.TextField(verbose_name = "подробности вопроса")
    author = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name='user', verbose_name = "автор")
    answers_count = models.IntegerField(default=0, verbose_name = "ответы")
    rating = models.IntegerField(default=0, verbose_name = "рейтинг")
    views = models.IntegerField(default=0, verbose_name = "просмотры")
    creation_time = models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания')
    published = models.BooleanField(default=True, verbose_name="опубликован?")
    tags = models.ManyToManyField('Tags', blank=True, related_name='tags', verbose_name='Теги')

    def __str__(self):
        return self.question

    objects = QuestManager()

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

class Answers(models.Model):
    answer = models.TextField(verbose_name = "текст ответа")
    question = models.ForeignKey(
        Questions, on_delete=models.CASCADE, verbose_name = "вопрос")
    author = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name='answers', verbose_name = "автор")
    creation_time = models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания')
    right_answer = models.BooleanField(default=False, verbose_name="верный ответ")

    def __str__(self):
        return "{} -> {}".format(self.answer, self.question)

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"

class Tags(models.Model):
    tag = models.CharField(max_length=20, verbose_name="тег")
    author = models.ForeignKey(
        Users, on_delete=models.CASCADE, verbose_name = "добавил тег")
    questions_count = models.IntegerField(default=0, verbose_name = "вопросы")
    # questions = models.ManyToManyField('Questions', blank=True, related_name='quest', verbose_name='Voprosi')

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


# class QuestTag(models.Model):
#     question = models.ForeignKey(
#         Questions, on_delete=models.CASCADE, verbose_name = "вопрос")
#     tag = models.ForeignKey(
#         Tags, on_delete=models.CASCADE, verbose_name = "тег")

#     def __str__(self):
#         return "{} -> {}".format(self.question, self.tag)