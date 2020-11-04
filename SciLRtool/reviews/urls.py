# coding: utf-8

from django.conf.urls import include, url
from django.urls import path
from SciLRtool.reviews.views import *


urlpatterns = [
    url(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/$', review, name='review'),
    url(r'^(?P<username>[^/]+)/$', reviews, name='reviews'),
    url(r'^new/$', new, name='new'),
    url(r'^add_author/$', add_author_to_review, name='add_author_to_review'),
    url(r'^remove_author/$', remove_author_from_review, name='remove_author_from_review'),
    url(r'^save_description/$', save_description, name='save_description'),
    url(r'^leave/$', leave, name='leave'),

    url(r'^planning/', include('SciLRtool.reviews.planning.urls')),
    url(r'^conducting/', include('SciLRtool.reviews.conducting.urls')),
    url(r'^reporting/', include('SciLRtool.reviews.reporting.urls')),
    url(r'^reporting/', include('SciLRtool.reviews.settings.urls')),

    url('', include('SciLRtool.reviews.planning.urls')),
    url('', include('SciLRtool.reviews.conducting.urls')),
    url('', include('SciLRtool.reviews.reporting.urls')),
    url('', include('SciLRtool.reviews.settings.urls')),
]
