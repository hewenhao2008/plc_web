# coding=u8
import datetime
import json

from django.contrib.auth.models import User
from django.template.loader import get_template
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response

import requests

DATA_SERVER_HOST = 'http://1.yakumo.applinzi.com'


# Create your views here.
def index(request):
    return HttpResponse('hello, world!')


def npm(request):
    return redirect('http://localhost:8080/__webpack_hmr')


# def page1(request):
#     return render(request, )

def current_datetime(request):
    dt = datetime.datetime.now()
    html = '现在的时间是{}'.format(dt)
    return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "{}小时后的时间为{}".format(offset, dt)
    return HttpResponse(html)


def yunji_1(request):
    # t = get_template('p1.php')
    return HttpResponse('p1.html')


class APIBase(APIView):
    def __init__(self, path):
        super(APIBase, self).__init__()
        self.PATH = path
        self.url = DATA_SERVER_HOST + self.PATH

    def get(self, request):
        res = requests.get(self.url)
        print(res.raw)
        data = res.json()
        return Response(data)

    def post(self, request):
        param = json.loads(request.body)
        print(param)
        res = requests.post(self.url, json=param)
        data = res.json()
        return Response(data)

    def put(self, request):
        print(request.body)
        param = json.loads(request.body)
        print(param)
        res = requests.put(self.url, json=param)
        print(res.status_code)
        data = res.json()
        print(data)
        return Response(data)

    def delete(self, request):
        param = json.loads(request.body)
        print(param)
        res = requests.delete(self.url, json=param)
        data = res.json()
        return Response(data)


class APIRegister(APIView):
    def put(self, request):
        data = json.loads(request.body)
        username = data['username']
        email = data['email']
        password = data['password']
        user = User.objects.create_user(username, email, password)
        user.save()
        data = {'msg': '注册成功'}
        return Response(data)


class APIStation(APIBase):
    def __init__(self):
        path = '/api/station'
        super(APIStation, self).__init__(path)


class APIPLC(APIBase):
    def __init__(self):
        path = '/api/plc'
        super(APIPLC, self).__init__(path)


class APIGroup(APIBase):
    def __init__(self):
        path = '/api/group'
        super(APIGroup, self).__init__(path)


class APIVariable(APIBase):
    def __init__(self):
        path = '/api/variable'
        super(APIVariable, self).__init__(path)


class APIValue(APIBase):
    def __init__(self):
        path = '/api/value'
        super(APIValue, self).__init__(path)


class APIAlarm(APIBase):
    def __init__(self):
        path = '/api/alarm'
        super(APIAlarm, self).__init__(path)


class APIQuery(APIBase):
    def __init__(self):
        path = '/api/query'
        super(APIQuery, self).__init__(path)


class APIAlarmLog(APIBase):
    def __init__(self):
        path = '/api/alarm_log'
        super(APIAlarmLog, self).__init__(path)


class APIAlarmInfo(APIBase):
    def __init__(self):
        path = '/api/alarm_info'
        super(APIAlarmInfo, self).__init__(path)


class APIParam(APIBase):
    def __init__(self):
        path = '/api/param'
        super(APIParam, self).__init__(path)
