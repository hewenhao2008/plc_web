"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.views.generic.base import TemplateView

from django.contrib.auth.models import User, Group

from django.contrib import admin

admin.autodiscover()

from rest_framework import permissions, routers, serializers, viewsets

from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope
from plc_web.views import index, current_datetime, hours_ahead, yunji_1, npm, github_auth, github_redirect


# first we define the serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    # url(r'^time/$', current_datetime),
    # url(r'^time/plus/(\d{1,2})$', hours_ahead),
    # url(r'^yunji/1/$', TemplateView.as_view(template_name='p1.html')),
    # url(r'^vue/2/$', TemplateView.as_view(template_name='vue_test.html')),
    # url(r'^yunji/$', TemplateView.as_view(template_name='vue.html')),
    url(r'^api/', include('plc_web.urls')),
    url(r'^__webpack_hmr/$', npm),
    url(r'^oauth/github$', github_auth, name="auth"),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^', include(router.urls)),
    url(r'^redirect$', github_redirect, name="redirect"),

]
