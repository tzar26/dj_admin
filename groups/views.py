# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from groups.models import Group
from accounts.models import Account
import json

def get_groups(request):
    #TODO: проверка token и его состояния просрочки
    objects = Group.objects.filter(account = Account.objects.get(login = 'sas2'))

    response_data = {}
    groups = []
    for obj in objects:
        groups.append({
            'id': str(obj.id),
            'name': obj.name,
        })
    response_data['quantity'] = len(groups)
    response_data['groups'] = groups
    return HttpResponse(json.dumps(response_data), content_type="application/json")
