# coding: utf-8

from django.conf.urls import url
from SciLRtool.reviews.settings.views import *


urlpatterns = [
    url(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/settings/$', settings, name='settings'),
    url(r'^review_settings/transfer/$', transfer, name='transfer_review'),
    url(r'^review_settings/delete/$', delete, name='delete_review'),
]
