# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Question(models.Model):
    category = models.ForeignKey(Category)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text
