from django.contrib import admin

from questions.models import Category, Question, Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Category)
admin.site.register(Question, QuestionAdmin)