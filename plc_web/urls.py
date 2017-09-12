# coding=u8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^test/', views.APIVariable.as_view(), name='test_api'),
    url(r'^register/', views.APIRegister.as_view(), name='api_register'),
    url(r'^plc/', views.APIPLC.as_view(), name='api_plc'),
    url(r'^group/', views.APIGroup.as_view(), name='api_group'),
    url(r'^variable/', views.APIVariable.as_view(), name='api_variable'),
    url(r'^value/', views.APIValue.as_view(), name='api_value'),
    url(r'^alarm/', views.APIAlarm.as_view(), name='api_alarm'),
    url(r'^query/', views.APIQuery.as_view(), name='api_query'),
    url(r'^alarm_log/', views.APIAlarmLog.as_view(), name='api_alarm_log'),
    url(r'^alarm_info/', views.APIAlarmInfo.as_view(), name='api_alarm_info'),
    url(r'^station/', views.APIStation.as_view(), name='api_station'),
    url(r'^param/', views.APIParam.as_view(), name='api_param'),
]
