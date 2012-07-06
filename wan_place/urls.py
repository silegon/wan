from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('',
    url('^place_detail/$', 'wan_place.views.place_detail'),
    url('^add_place_detail/$', 'wan_place.views.add_place_detail'),
    url('^edit_place_detail/$', 'wan_place.views.edit_place_detail'),
    url('', 'wan_place.views.index'),
    )
                      
