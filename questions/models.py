# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from groups.models import Group

class Category(models.Model):
    name = models.CharField('название категории', max_length=200)
    group = models.ManyToManyField(Group, verbose_name='группы')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __unicode__(self):
        return self.name

class Question(models.Model):
    category = models.ForeignKey(Category, verbose_name='категория вопроса')
    question = models.CharField('вопрос', max_length=200)
    answer = models.CharField('верный ответ', max_length=200)

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'

    def __unicode__(self):
        return self.question

class Choice(models.Model):
    question = models.ForeignKey(Question, verbose_name='вопрос')
    choice_text = models.CharField('выбор', max_length=200)

    class Meta:
        verbose_name = 'альтернативый верному выбор'
        verbose_name_plural = 'альтернативые верным выборы'

    def __unicode__(self):
        return self.choice_text
