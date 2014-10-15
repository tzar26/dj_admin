# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from groups.models import Group
from accounts.models import Account
# from django.conf import settings
# from accounts.views import login_required
import json

# @login_required
def get_groups(request):
    objects = Group.objects.filter(account = Account.objects.get(login = 'sas2'))
    # obj = Group.objects.filter(user = Account.objects.get(login = request.GET.get('username')))

    response_data = {}
    groups = []
    for obj in objects:
        groups.append({
            'id': str(obj.id),
            'name': obj.name,
        })
    response_data['quantity'] = len(groups)
    response_data['groups'] = groups
    # else:
    #     response_data['error'] = 'no groups for user'
    return HttpResponse(json.dumps(response_data), content_type="application/json")