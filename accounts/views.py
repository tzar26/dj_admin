# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from accounts.models import Account, Session
import json
import os

def get_credentials(username=None, password=None):
    if (not(username and password)):
        return { 'error': 'not enough credentials'}

    credentials = Account.objects.filter(login=username).filter(password=password)
    if credentials.count() < 1:
        return { 'error': 'login or password is incorrect'}

    response_data = {}
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


def login(request):
    def generate_token():
        return ''.join([hex(ord(c)).replace('0x','') for c in os.urandom(16)])
    username = request.GET.get('username')
    password = request.GET.get('password')
    user = get_credentials(username=username, password=password)
    if not user.get('error'):
        token = generate_token()
        session = Session(
            user = Account.objects.get(login = username),
            token = token,
        )
        session.save()
        response = HttpResponseRedirect(request.path)
        response.set_cookie('token', token)
        return HttpResponse(json.dumps({'token': token}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({'error': 'login or password incorrect'}), content_type="application/json")

from django.core.exceptions import ObjectDoesNotExist
def logout(request):
    token = request.GET.get('token')
    if not token:
        return HttpResponse(json.dumps({'error': 'incorrect request'}), content_type="application/json")

    try:
        session = Session.objects.get(token=token)
        session.delete()
        return HttpResponse(json.dumps({'message': 'logged out'}), content_type="application/json")
    except ObjectDoesNotExist, ex:
        return HttpResponse(json.dumps({'error': 'unactual request'}), content_type="application/json")
    except Exception, ex:
        return HttpResponse(json.dumps({'error': 'unknown error, try later'}), content_type="application/json")
