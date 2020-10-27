from django.conf.urls import url
from SciLRtool.core.views import *
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='core/about.html'), name='about'),
]
