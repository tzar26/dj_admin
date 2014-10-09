# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from questions.models import Question, Category

class Command(BaseCommand):
    categories_prefix = 'категория '
    categories_pool_length = 3
    questions_prefix = 'вопрос '
    questions_pool_length = 20

    def handle(self, *args, **options):
        for i in range(0, self.categories_pool_length):
            category = Category(name = self.categories_prefix + str(i + 1) )
            category.save()
        import random
        for i in range(0, self.questions_pool_length):
            a = random.randint(0,20)
            b = random.randint(0,20)
            answer = a+b
            question_text = '%s %s. Введите правильный ответ в выражении %s+%s' % (self.questions_prefix, i, a, b)
            question = Question(
                category = Category.objects.get(id = random.randint(1, self.categories_pool_length)),
                question = question_text,
                answer = str(answer)
            )
            question.save()
        print 'Фейковая база наполнена'
