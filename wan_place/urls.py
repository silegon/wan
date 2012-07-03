from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('',
    url('index/$', 'wan_place.views.index'),
    )
                      
