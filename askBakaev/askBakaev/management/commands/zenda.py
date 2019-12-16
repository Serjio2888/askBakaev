from django.core.management.base import BaseCommand
from django.db import transaction

from main.models import Questions
from main.models import Tags
from main.models import Users
from main.models import Answers

from datetime import datetime
import random
from datetime import timedelta

names = ['kir', 'serg', 'andrew', 'max', 'dinar', 'sergey', 'egor', 'evgeny', 'anna', 'lee']
words = ['beautiful', 'angry', 'strong', 'weak', 'handsome', 'poor', ' fast', 'lazy', 'big']
random_users = Users.objects.all()  # [random.randint(0,100):random.randint(100,200)]
random_tags = Tags.objects.all()  # [random.randint(0,15):random.randint(19,100)]
random_questions = Questions.objects.all()  # [random.randint(0,105):random.randint(150,1000)]

class Command(BaseCommand):
    help = 'Random info adder'

    @transaction.atomic
    def handle(self, *args, **options):
        if options['users']:
            how_many = int(options['users'])
            if how_many > 0:
                name = None
                now = datetime.now()
                for i in range(how_many):  
                    desc = random.choice(words)+' '+random.choice(words)
                    naming = random.choice(names)+str(random.randint(0, how_many))
                    q = Users.objects.create(name=naming, birthday=now, 
                            about=desc, avatar='avatar', password=desc+naming)
                q.save()
                print(how_many, "users inserted")
                print(str(datetime.now()-now), "time spent")

        if options['quests']:
            how_many = int(options['quests'])
            if how_many > 0:
                name = None
                now = datetime.now()
                for i in range(how_many): 
                    nice_num = random.randint(1, 1449)
                    timer = now-timedelta(nice_num)
                    question = 'is '+random.choice(words)+' '+random.choice(words)+'?'
                    description = (random.choice(names)+str(random.randint(0, how_many)))*2
                    author = random.choice(random_users)
                    tags = [random.choice(random_tags) for _ in range(3)]
                    q = Questions.objects.create(question=question, description=description,author=author,
                            rating=nice_num, views=nice_num, creation_time=timer)
                    q.tags.set(tags)
                q.save()
                print(how_many, "questions inserted")
                print(str(datetime.now()-now), "time spent")

        if options['tags']:
            how_many = int(options['tags'])
            if how_many > 0:
                name = None
                now = datetime.now()
                for i in range(how_many): 
                    nice_num = random.randint(500, 1449)
                    author = random.choice(random_users)
                    tag = random.choice(words)+str(nice_num)
                    q = Tags.objects.create(tag=tag, author=author)
                q.save()
                print(how_many, "tags inserted")
                print(str(datetime.now()-now), "time spent")

        if options['answers']:
            how_many = int(options['answers'])
            if how_many > 0:
                name = None
                now = datetime.now()
                for i in range(how_many): 
                    nice_num = str(random.randint(500, 1449))
                    author = random.choice(random_users)
                    q = Answers.objects.create(answer="i don't know "+nice_num, author=author,
                                                question=random.choice(random_questions))
                q.save()
                print(how_many, "answers inserted")
                print(str(datetime.now()-now), "time spent")

    def add_arguments(self, parser):
        parser.add_argument(
        '-u', 
        '--users',
        action='store', 
        default=False,
        help='Добавление рандомных юзеров'
        )
        parser.add_argument(
        '-q', 
        '--quests',
        action='store', 
        default=False,
        help='Добавление рандомных вопросов'
        )
        parser.add_argument(
        '-t', 
        '--tags',
        action='store', 
        default=False,
        help='Добавление рандомных tags'
        )
        parser.add_argument(
        '-a', 
        '--answers',
        action='store', 
        default=False,
        help='Добавление рандомных answers'
        )