# -*- coding: utf-8 -*-
from django.contrib import admin
from groups.models import Group
# from accounts.admin import AccountsInline

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    model = Group
    fk_name = 'типа группа'
    # inlines = [AccountsInline]
