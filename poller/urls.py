
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^poller/$', 'poller.views.index'),
	url(r'^poller/(?P<poll_id>\d+)/$', 'poller.views.detail'),
	url(r'^poller/(?P<poll_id>\d+)/results/$', 'poller.views.results'),
	url(r'^poller/(?P<poll_id>\d+)/vote/$', 'poller.views.vote'),
    url(r'^admin/', include(admin.site.urls)),
)
