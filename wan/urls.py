from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^static/(.*)$', 'django.views.static.serve',{'document_root':settings.STATIC_ROOT, 'show_indexes':True}),
    url(r'^media/(.*)$', 'django.views.static.serve',{'document_root':settings.MEDIA_ROOT, 'show_indexes':True}),
    url(r'^favicon\.ico$','django.views.generic.simple.redirect_to',
        {'url':'/static/img/favicon.ico'}),
    url(r'^place/', include('wplace.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
