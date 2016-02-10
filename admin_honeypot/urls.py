import django
from admin_honeypot import views

try:
    from django.conf.urls import patterns, url
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import patterns, url

if django.VERSION >= (1, 7):
    urlpatterns = []
    urlpatterns += [
        url(r'^login/$', views.AdminHoneypot.as_view(), name='login'),
        url(r'^.*$', views.AdminHoneypot.as_view(), name='index'),
    ]
else:
    urlpatterns = patterns('')
    urlpatterns += patterns('',
        url(r'^.*$', views.AdminHoneypot.as_view(), name='index'),
    )
