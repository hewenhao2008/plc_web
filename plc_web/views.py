# coding=u8
import datetime
import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.template.loader import get_template
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.admin import TokenAdmin

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.views import ObtainAuthToken

import requests

DATA_SERVER_HOST = 'http://1.yakumo.applinzi.com'

TokenAdmin.raw_id_fields = ('user',)


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
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def __init__(self, path):
        super(APIBase, self).__init__()
        self.PATH = path
        self.url = DATA_SERVER_HOST + self.PATH

    def get(self, request):
        # print(request.META)
        res = requests.get(self.url)
        print(res.raw)
        data = res.json()
        return Response(data)

    def post(self, request):
        param = json.loads(request.body)
        print(param)
        res = requests.post(self.url, json=param)
        data = res.json()
        return Response(data, headers={'Access-Control-Allow-Headers': '*'})

    def put(self, request):
        print(request.body)
        param = json.loads(request.body)
        print(param)
        res = requests.put(self.url, json=param)
        print(res.status_code, res.content)
        data = res.json()
        print(data)
        return Response(data, headers={'Access-Control-Allow-Headers': '*'})

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


class ExampleView(APIView):
    # authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        content = {
            'user': unicode(request.user),  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),  # None
        }
        return Response(content)


class UserManage(APIView):
    # authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = json.loads(request.body)
        print(request.user)
        username = data['username']
        password = data['password']
        print('a')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                print(token.key, created)
                res = {
                    'msg': u'登录成功',
                    'token': token.key,
                    'username': user.username,
                    'email': user.email
                }
                return Response(res)
            else:
                res = {'msg': u'未激活'}
                return Response(res)
        else:
            res = {'msg': u'登录失败'}
            return Response(res)

    def put(self, request):
        data = json.loads(request.body)
        username = data['username']
        email = data['email']
        password = data['password']
        user = User.objects.create_user(username, email, password)
        user.save()
        data = {'msg': u'注册成功'}
        return Response(data)


# github 认证
def github_redirect(request):
    import random
    random_string = str(random.randint(1, 10))
    request.session['github_state'] = random_string
    redirect_url = settings.GITHUB_REDIRECT + "?client_id=" + \
                   settings.GITHUB_CLIENT_ID + "&redirect_uri=" + settings.REDIRECT_URL \
                   + "&state=" + random_string
    return HttpResponseRedirect(redirect_url)


def github_auth(request):
    code = request.GET.get('code')
    state = request.GET.get('state')
    print(dict(request.session))
    save_state = request.session.get('github_state', "no")
    if save_state == state:
        params = {"client_id": settings.GITHUB_CLIENT_ID, "client_secret": settings.GITHUB_CLIENT_SECERT, \
                  "code": code, "state": state, "redirect_uri": settings.REDIRECT_URL}
        headers = {"Accept": "application/json"}
        url = settings.GITHUB_REDIRECT_EXCHANGE
        r = requests.post(url, params=params, headers=headers)
        access_token = r.json()['access_token']
        params = {"access_token": access_token}
        r = requests.get(settings.GITHUB_API, params=params)
        json_result = r.json()
        return render(request, 'index.html', {"result": json_result})
        # return HttpResponse('hello, world!')
    else:
        raise Http404()
