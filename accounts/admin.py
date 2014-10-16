# -*- coding: utf-8 -*-
from django.contrib import admin
from accounts.models import Account, Session
import re

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    model = Account
    list_display = ('login', 'group_list')
    filter_horizontal = ('group',)

    # def get_fields(self, request, obj):
    #     # import pdb; pdb.set_trace()
    #     # obj.password = re.sub(r'.', '*', obj.password)
    #     return obj

    def group_list(self, obj):
        return ','.join(obj.group.values_list('name', flat=True))

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    model = Session
    list_display = ('user','token')
    readonly_fields = ('user','token')

#Скрываем блок штатной аутентификации групп и пользователей
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
admin.site.unregister(User)
admin.site.unregister(Group)
