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
from django.contrib import admin
from django.views.generic.base import TemplateView

from plc_web.views import index, current_datetime, hours_ahead, yunji_1, npm

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})$', hours_ahead),
    url(r'^yunji/1/$', TemplateView.as_view(template_name='p1.html')),
    url(r'^vue/2/$', TemplateView.as_view(template_name='vue_test.html')),
    url(r'^yunji/$', TemplateView.as_view(template_name='vue.html')),
    url(r'^api/', include('plc_web.urls')),
    url(r'^__webpack_hmr/$', npm)
]
