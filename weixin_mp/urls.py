from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from myTest.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'weixin_mp.views.home', name='home'),
    # url(r'^weixin_mp/', include('weixin_mp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #url(r'^weixin/$', 'weixin.views.weixin_main'),
    url(r'^$', 'weixin.views.weixin_main'),
    url(r'^co_search/$', 'myTest.views.co_search'),
    url(r'^product_search/$', 'myTest.views.product_search'),
    # url(r'^hello/(\d+)/$', 'myTest.views.hello1'),


)
