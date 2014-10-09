# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
import json

# from users.models import User
from django.contrib import auth

def get_credentials(request):
    # import pdb;pdb.set_trace()
    # if (not(request.GET.get('login') and request.GET.get('pass'))):
    #     return HttpResponse(json.dumps({ 'error': 'not enough credentials'}), content_type="application/json")

    credentials = auth.authenticate(username=request.GET.get('login'), password=request.GET.get('pass'))
    # credentials = User.objects.filter(login=request.GET.get('login')).filter(password=request.GET.get('pass'))
    # if credentials.count() < 1:
    #     return HttpResponse(json.dumps({ 'error': 'login or password is incorrect'}), content_type="application/json")

    response_data = {}
    if credentials is not None:
        response_data['username'] = credentials.username
        response_data['avatar'] = credentials.gameuser.avatar
    else:
        response_data['error'] = 'login or password is incorrect'
    return HttpResponse(json.dumps(response_data), content_type="application/json")
