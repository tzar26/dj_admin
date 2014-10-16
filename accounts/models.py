# -*- coding: utf-8 -*-
from django.db import models
from groups.models import Group
from django.utils.translation import ugettext as _
from django.conf import settings
from datetime import datetime, timedelta
from re import sub as re_sub

class Account(models.Model):
    login = models.CharField('логин', max_length=30)
    password = models.CharField('пароль', max_length=50)
    avatar = models.CharField('аватар',max_length=150)
    group = models.ManyToManyField(Group, null=True, verbose_name=u'группы')
    reg_date = models.DateTimeField('дата регистрации', default=datetime.today)

    class Meta:
        verbose_name = 'учётная запись'
        verbose_name_plural = 'учётные записи'

    def __unicode__(self):
        return self.login

    # def password_view(self):
    #     return re_sub(r'.', '*', self.password)
    # password_view.short_description = 'password view for admin site'
    # password_view.allow_tags = True
    # password2 = property(password_view)

def expired_time():
    return datetime.today() + timedelta(minutes=settings.SESSION_EXPIRED_MINUTES)

class Session(models.Model):
    token = models.CharField('токен', max_length=32)
    user = models.ForeignKey(Account, verbose_name='пользователь')
    expired = models.DateTimeField('сессия истекает', default=expired_time)

    class Meta:
        verbose_name = 'сессия'
        verbose_name_plural = 'сессии'
