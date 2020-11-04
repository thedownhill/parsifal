# coding: utf-8

from django.conf.urls import url
from SciLRtool.reviews.reporting.views import *


urlpatterns = [
    url(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/reporting/$', reporting, name='reporting'),
    url(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/reporting/export/$', export, name='export'),
    # url(r'^download_docx/$', download_docx, name='download_docx'),
]
