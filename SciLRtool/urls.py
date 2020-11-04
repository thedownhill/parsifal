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
