# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from questions.models import Category, Question, Choice
import json

# def get_question(request):
#     # import pdb;pdb.set_trace()
#     if request.GET.get('category'):
#         question = Question.objects.filter(category=request.GET.get('category')).order_by('?')[0]
#     else:
#         question = Question.objects.all().order_by('?')[0]
#     response_data = {}
#     response_data['id'] = question.id
#     response_data['question'] = question.question
#     response_data['rightansw'] = question.rightansw
#     response_data['choices'] = [ response_data['rightansw'] ]
#     response_data['choices'].extend(set(choice for (id,cat,choice,vote) in question.choice_set.values_list()))
#     return HttpResponse(json.dumps(response_data), content_type="application/json")

# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
# from django.http import HttpResponse
# from questions.models import Category, Question, Choice
# import json

def get_question(request):
    # import pdb;pdb.set_trace()
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
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def get_poll(request):
    pass