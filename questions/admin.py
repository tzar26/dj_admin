# -*- coding: utf-8 -*-
from django.contrib import admin
from questions.models import Category, Question, Choice

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('name', 'group_list')
    filter_horizontal = ('group',)

    def group_list(self, obj):
        return ','.join(obj.group.values_list('name', flat=True))


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question', 'category')
