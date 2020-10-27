from django.conf.urls import url
from SciLRtool.authentication.views import *
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView

urlpatterns = [
    url(r'^signup/$', signup, name='signup'),
    url(r'^signin/$', signin, name='signin'),
    url(r'^signout/$', signout, name='signout'),
    url(r'^reset/$', PasswordResetView.as_view(), name='reset'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^success/$', success, name='success'),
]
