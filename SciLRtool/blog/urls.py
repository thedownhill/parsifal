# coding: utf-8

from django.conf.urls import url
from SciLRtool.blog.views import *

urlpatterns = [
    url(r'^$', entries, name='entries'),
    url(r'^(?P<slug>[-\w]+)/$', entry, name='entry'),
]
