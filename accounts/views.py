# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from accounts.models import Account, Session
import json
import os

# from users.models import Account
from django.contrib import auth

def get_credentials(username=None, password=None):
    if (not(username and password)):
        return { 'error': 'not enough credentials'}

    credentials = Account.objects.filter(login=username).filter(password=password)
    if credentials.count() < 1:
        return { 'error': 'login or password is incorrect'}

    response_data = {}
    # import pdb;pdb.set_trace()
    if credentials is not None:
        credential = credentials[0]
        response_data['username'] = credential.login
        response_data['avatar'] = credential.avatar
        groups = []
        for group in credential.group.values():
            groups.append({
                'id': str(group['id']),
                'name': group['name'],
            })
        response_data['groups'] = groups
    else:
        response_data['error'] = 'login or password is incorrect'
    return response_data
    # return HttpResponse(json.dumps(response_data), content_type="application/json")

from django.shortcuts import render_to_response

def token_required(request):
    pass

def generate_token():
    return ''.join([hex(ord(c)).replace('0x','') for c in os.urandom(16)])

def login(request):
    pass

def login_required(request):
    return
    # if request.COOKIES.get('token') is not None:
    #     return HttpResponseRedirect(request.path)
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = get_credentials(username=username, password=password)
    if not user.get('error'):
        import pdb;pdb.set_trace()
        token = generate_token()
        session = Session(
            user = Account.objects.get(login = username),
            token = token
        )
        session.save()
        response = HttpResponseRedirect(request.path)
        response.set_cookie('token', token)
        return response
    else:
        return render(request, 'login.html', {})
        # return render_to_response("login.html")

def logout(request):
    response = HttpResponseRedirect('/groups')
    if request.COOKIES.get('token') is not None:
        response.delete_cookie('token')
    # Перенаправление на страницу.
    return response