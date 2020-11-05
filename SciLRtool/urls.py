# coding: utf-8

from django.urls import include, path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin

# admin.autodiscover()

urlpatterns = [
    path('', include('SciLRtool.core.urls')),
    path('', include('SciLRtool.authentication.urls')),

    path('admin/', admin.site.urls),

    path('reviews/', include(('SciLRtool.reviews.urls', 'SciLRtool.reviews'), namespace='reviews')),
    path('activity/', include(('SciLRtool.activities.urls', 'SciLRtool.activities'), namespace='activities')),
    path('blog/', include(('SciLRtool.blog.urls', 'SciLRtool.blog'), namespace='blog')),
    path('help/', include(('SciLRtool.help.urls', 'SciLRtool.help'), namespace='help')),
    path('library/', include(('SciLRtool.library.urls', 'SciLRtool.library'), namespace='library')),
    path('settings/', include(('SciLRtool.account_settings.urls', 'SciLRtool.account_settings'), namespace='settings')),

    path('', include('SciLRtool.reviews.urls')),
    path('', include('SciLRtool.activities.urls')),
    path('', include('SciLRtool.blog.urls')),
    path('', include('SciLRtool.help.urls')),
    path('', include('SciLRtool.library.urls')),
    path('', include('SciLRtool.account_settings.urls')),

    url(r'^sitemap.xml$', TemplateView.as_view(template_name='sitemap.xml', content_type='application/xml')),
    url(r'^robots.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#
# from django.conf.urls import include, url
# from django.conf import settings
# from django.conf.urls.static import static
# from django.views.generic import TemplateView
# from django.contrib import admin
# from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
#
# from SciLRtool import authentication, core, settings, reviews, activities
#
# admin.autodiscover()
#
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#
#     url(r'^$', core.views.home, name='home'),
#     url(r'^about/$', TemplateView.as_view(template_name='core/about.html'), name='about'),
#     url(r'^signup/$', authentication.views.signup, name='signup'),
#     url(r'^signin/$', authentication.views.signin, name='signin'),
#     url(r'^signout/$', authentication.views.signout, name='signout'),
#
#     # url(r'^reset/$', authentication.views.reset, name='reset'),
#     # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
#     #     authentication.views.reset_confirm, name='password_reset_confirm'),
#     url(r'^reset/$', PasswordResetView.as_view(), name='reset'),
#     url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
#         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#
#     url(r'^success/$', authentication.views.success, name='success'),
#     url(r'^reviews/', include(('SciLRtool.reviews.urls', 'SciLRtool.reviews'), namespace='reviews')),
#     url(r'^activity/', include(('SciLRtool.activities.urls', 'SciLRtool.activities'), namespace='activities')),
#     url(r'^blog/', include(('SciLRtool.blog.urls', 'SciLRtool.blog'), namespace='blog')),
#     url(r'^help/', include(('SciLRtool.help.urls', 'SciLRtool.help'), namespace='help')),
#     url(r'^library/', include(('SciLRtool.library.urls', 'SciLRtool.library'), namespace='library')),
#     url(r'^settings/', include(('SciLRtool.account_settings.urls', 'SciLRtool.account_settings'), namespace='settings')),
#     url(r'^review_settings/transfer/$', reviews.settings.views.transfer, name='transfer_review'),
#     url(r'^review_settings/delete/$', reviews.settings.views.delete, name='delete_review'),
#
#     url(r'^sitemap.xml$',
#         TemplateView.as_view(template_name='sitemap.xml', content_type='application/xml')),
#     url(r'^robots.txt$',
#         TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
#
#     url(r'^(?P<username>[^/]+)/following/$', activities.views.following, name='following'),
#     url(r'^(?P<username>[^/]+)/followers/$', activities.views.followers, name='followers'),
#
#     # Review URLs
#     url(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/$', reviews.views.review, name='review'),
#     url(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/settings/$', reviews.settings.views.settings,
#         name='settings'),
#
#     # Planning Phase
#     url(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/planning/$', reviews.planning.views.planning,
#         name='planning'),
#     url(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/planning/protocol/$',
#         reviews.planning.views.protocol, name='protocol'),
#     url(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/planning/quality/$',
#         reviews.planning.views.quality_assessment_checklist, name='quality_assessment_checklist'),
#     url(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/planning/extraction/$',
#         reviews.planning.views.data_extraction_form, name='data_extraction_form'),
#
#     # Conducting Phase
#     url(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/conducting/$',
#         reviews.conducting.views.conducting, name='conducting'),
#     url(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/conducting/search/$',
#         reviews.conducting.views.search_studies, name='search_studies'),
#     url(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/conducting/import/$',
#         reviews.conducting.views.import_studies, name='import_studies'),
#     url(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/conducting/studies/$',
#         reviews.conducting.views.study_selection, name='study_selection'),
#     url(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/conducting/quality/$',
#         reviews.conducting.views.quality_assessment, name='quality_assessment'),
#     url(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/conducting/extraction/$',
#         reviews.conducting.views.data_extraction, name='data_extraction'),
#     url(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/conducting/analysis/$',
#         reviews.conducting.views.data_analysis, name='data_analysis'),
#
#     # Reporting Phase
#     url(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/reporting/$',
#         reviews.reporting.views.reporting, name='reporting'),
#     url(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/reporting/export/$',
#         reviews.reporting.views.export, name='export'),
#
#     url(r'^(?P<username>[^/]+)/$', reviews.views.reviews, name='reviews'),
# ]
#
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
