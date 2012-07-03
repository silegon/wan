from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^static/(.*)$', 'django.views.static.serve',{'document_root':settings.STATIC_ROOT, 'show_indexes':True}),
    url(r'^media/(.*)$', 'django.views.static.serve',{'document_root':settings.MEDIA_ROOT, 'show_indexes':True}),
    url(r'^place/', include('wan_place.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
