# coding: utf-8

from django.urls import include, path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin

from SciLRtool import core, authentication, reviews, activities
from SciLRtool.core import views as core_views


admin.autodiscover()

urlpatterns = [
    ### core
    path('', include('SciLRtool.core.urls')),
    # authentication
    path('', include('SciLRtool.authentication.urls')),

    path(r'^admin/', include(admin.site.urls)),
    path(r'^reviews/', include('SciLRtool.reviews.urls', namespace='reviews')),
    path(r'^activity/', include('SciLRtool.activities.urls', namespace='activities')),
    path(r'^blog/', include('SciLRtool.blog.urls', namespace='blog')),
    path(r'^help/', include('SciLRtool.help.urls', namespace='help')),
    path(r'^library/', include('SciLRtool.library.urls', namespace='library')),
    path(r'^settings/', include('SciLRtool.account_settings.urls', namespace='settings')),

    url(r'^review_settings/transfer/$', 'reviews.settings.views.transfer', name='transfer_review'),
    url(r'^review_settings/delete/$', 'reviews.settings.views.delete', name='delete_review'),
    url(r'^sitemap.xml$', TemplateView.as_view(template_name='sitemap.xml', content_type='application/xml')),
    url(r'^robots.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    url(r'^(?P<username>[^/]+)/following/$', 'activities.views.following', name='following'),
    url(r'^(?P<username>[^/]+)/followers/$', 'activities.views.followers', name='followers'),

    # Review URLs
    url(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/$', 'reviews.views.review', name='review'),
    url(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/settings/$', 'reviews.settings.views.settings', name='settings'),

    # Planning Phase
    url(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/planning/$', 'reviews.planning.views.planning', name='planning'),
    url(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/planning/protocol/$', 'reviews.planning.views.protocol', name='protocol'),
    url(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/planning/quality/$', 'reviews.planning.views.quality_assessment_checklist', name='quality_assessment_checklist'),
    url(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/planning/extraction/$', 'reviews.planning.views.data_extraction_form', name='data_extraction_form'),

    # Conducting Phase
    url(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/conducting/$', 'reviews.conducting.views.conducting', name='conducting'),
    url(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/conducting/search/$', 'reviews.conducting.views.search_studies', name='search_studies'),
    url(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/conducting/import/$', 'reviews.conducting.views.import_studies', name='import_studies'),
    url(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/conducting/studies/$', 'reviews.conducting.views.study_selection', name='study_selection'),
    url(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/conducting/quality/$', 'reviews.conducting.views.quality_assessment', name='quality_assessment'),
    url(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/conducting/extraction/$', 'reviews.conducting.views.data_extraction', name='data_extraction'),
    url(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/conducting/analysis/$', 'reviews.conducting.views.data_analysis', name='data_analysis'),

    # Reporting Phase
    url(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/reporting/$', 'reviews.reporting.views.reporting', name='reporting'),
    url(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/reporting/export/$', 'reviews.reporting.views.export', name='export'),

    url(r'^(?P<username>[^/]+)/$', 'reviews.views.reviews', name='reviews'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
