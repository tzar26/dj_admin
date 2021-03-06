# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from questions.models import Category, Question, Choice
from django.conf import settings
import json


def req_question(request):
    if request.GET.get('category'):
        obj = Question.objects.filter(category=request.GET.get('category')).order_by('?')
    else:
        obj = Question.objects.all().order_by('?')

    response_data = {}
    if obj:
        question = obj[0]
        response_data['id'] = question.id
        response_data['question'] = question.question
        response_data['answer'] = question.answer
        response_data['choices'] = [ response_data['answer'] ]
        response_data['choices'].extend(set(choice for (id,cat,choice) in question.choice_set.values_list()))
    else:
        response_data['error'] = 'no questions in category(categories)'
    return response_data

def get_question(request):
    #TODO: проверка token и его состояния просрочки
    response_data = req_question(request)
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def get_poll(request):
    #TODO: проверка token и его состояния просрочки
    response_data = {}
    questions = []
    qids = []
    retry = 0
    while (len(questions)<settings.POLL_LENGTH) and (retry < settings.DUPLICATE_QUESTION_RETRY_ABORT):
        question = req_question(request)
        if question.get('error'):
            return HttpResponse(json.dumps(question), content_type="application/json")

        if not question.get('id') in qids:
            qids.append(question.get('id'))
            questions.append(question)
            retry = 0
        else:
            retry += 1
    response_data['quantity'] = len(questions)
    response_data['questions'] = questions
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def get_categories(request):
    #TODO: проверка token и его состояния просрочки
    objects = Category.objects.all()
    response_data = {}
    categories = []
    for obj in objects:
        categories.append({
            'id': obj.id,
            'name': obj.name
        })
    response_data['quantity'] = len(categories)
    response_data['categories'] = categories
    return HttpResponse(json.dumps(response_data), content_type="application/json")
