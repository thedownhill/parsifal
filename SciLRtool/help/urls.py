# coding: utf-8

from django.conf.urls import url
from SciLRtool.help.views import *

urlpatterns = [
    url(r'^$', articles, name='articles'),
    url(r'^search/$', search, name='search'),
    url(r'^(?P<slug>[-\w]+)/$', article, name='article'),
]
