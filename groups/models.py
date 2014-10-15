# -*- coding: utf-8 -*-
from django.db import models

class Group(models.Model):
    name = models.CharField('название группы', max_length=200)

    class Meta:
        verbose_name = 'группа пользователей'
        verbose_name_plural = 'группы пользователей'

    def __unicode__(self):
        return self.name
