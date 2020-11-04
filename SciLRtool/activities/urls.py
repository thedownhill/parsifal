# coding: utf-8
from django.conf.urls import url
from SciLRtool.activities.views import *

urlpatterns = [
    url(r'^follow/$', follow, name='follow'),
    url(r'^unfollow/$', unfollow, name='unfollow'),
    url(r'^update_followers_count/$', update_followers_count, name='update_followers_count'),
    url(r'^(?P<username>[^/]+)/following/$', following, name='following'),
    url(r'^(?P<username>[^/]+)/followers/$', followers, name='followers'),
]