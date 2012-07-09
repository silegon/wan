from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('',
    url('^place_detail/(\d+)$', 'wplace.views.place_detail'),
    url('^add_place_detail$', 'wplace.views.add_place_detail'),
    url('^edit_place_detail/(\d+)$', 'wplace.views.edit_place_detail'),
    url('^upload_file$', 'wplace.views.upload_file'),
    url('^index$', 'wplace.views.index'),
    )
                      
