# -*- coding: utf-8 -*-
from django.db import models
from groups.models import Group
from django.utils.translation import ugettext as _
from datetime import datetime

class Account(models.Model):
    login = models.CharField('логин', max_length=30)
    password = models.CharField('пароль', max_length=50)
    avatar = models.CharField('аватар',max_length=150)
    group = models.ManyToManyField(Group, verbose_name=u'группы')
    reg_date = models.DateTimeField('дата регистрации', default=datetime.today)

    class Meta:
        verbose_name = 'учётная запись'
        verbose_name_plural = 'учётные записи'

    def __unicode__(self):
        return self.login

class Session(models.Model):
    token = models.CharField('токен', max_length=30)
    user = models.ForeignKey(Account, verbose_name='пользователь')

    class Meta:
        verbose_name = 'сессия'
        verbose_name_plural = 'сессии'
