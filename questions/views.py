# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from questions.models import Category, Question, Choice
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
        response_data['choices'].extend(set(choice for (id,cat,choice,vote) in question.choice_set.values_list()))
    else:
        response_data['error'] = 'no questions in category(categories)'
    return response_data

def get_question(request):
    response_data = req_question(request)
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def get_poll(request):
    quantity = 10
    duplicate_retry_abort = 10
    # import pdb;pdb.set_trace()

    response_data = {}
    questions = []
    qids = []
    retry = 0
    while (len(questions)<10) and (retry < duplicate_retry_abort):
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
