# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from groups.models import Group
from questions.models import Question, Category, Choice

class Command(BaseCommand):
    groups_prefix = 'группа '
    groups_pool_length = 3
    categories_prefix = 'категория '
    categories_pool_length = 3
    questions_prefix = 'вопрос '
    questions_pool_length = 100

    def handle(self, *args, **options):
        Group.objects.all().delete()
        Category.objects.all().delete()
        Choice.objects.all().delete()
        Question.objects.all().delete()

        #сбрасываем автоинкремент чтобы не ловить индекс категории
        from django.db import connection
        cursor = connection.cursor()
        sql = 'ALTER TABLE groups_group AUTO_INCREMENT=1;'
        cursor.execute(sql)
        sql = 'ALTER TABLE questions_category AUTO_INCREMENT=1;'
        cursor.execute(sql)

        for i in range(0, self.groups_pool_length):
            group = Group(name = self.groups_prefix + str(i + 1) )
            group.save()
        print 'Таблица групп наполнена'

        for i in range(0, self.categories_pool_length):
            category = Category(name = self.categories_prefix + str(i + 1))
            category.save()
        print 'Таблица категорий наполнена'

        import random
        for i in range(0, self.questions_pool_length):
            a = random.randint(0,20)
            b = random.randint(0,20)
            answer = a+b
            question_text = '%s %s. Введите правильный ответ в выражении %s+%s' % (self.questions_prefix, i, a, b)
            question = Question(
                category = Category.objects.all().order_by('?')[0],
                question = question_text,
                answer = str(answer)
            )
            question.save()

            for j in range(3):
                choice = Choice(
                    question = question,
                    choice_text = answer + (-1)**random.randint(0,10)*random.randint(1,3)
                )
                choice.save()
        print 'Таблицы вопросов и выборов наполнены'
