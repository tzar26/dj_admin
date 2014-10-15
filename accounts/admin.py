# -*- coding: utf-8 -*-
from django.contrib import admin
# from myapp.widgets import RichTextEditorWidget
from accounts.models import Account, Session
# from groups.models import Group

# class AccountsInline(admin.TabularInline):
#     model = Account.group.through
#     verbose_name = 'группа'
#     verbose_name_plural = 'типа группы'

# class GroupsInline(admin.TabularInline):
#     model = Group.account_set.through
#     verbose_name = 'группа'
#     verbose_name_plural = 'группы'

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    model = Account
    list_display = ('login', 'group_list')
    # inlines = [GroupsInline]
    # formfield_overrides = {
    #     models.TextField: {'widget': RichTextEditorWidget},
    # }

    def group_list(self, obj):
        return ','.join(obj.group.values_list('name', flat=True))

    # def formfield_for_manytomany(self, db_field, request, **kwargs):
    #     if db_field.name == "group":
    #         kwargs["queryset"] = Group.objects.filter(user=request.user)
    #     return super(AccountAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

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
