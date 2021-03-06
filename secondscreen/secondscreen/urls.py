from django.contrib import admin
from django.conf.urls import patterns, include, url

import views

# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#hooking-adminsite-instances-into-your-urlconf
admin.autodiscover()


# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = patterns('',
    # Admin panel and documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', views.home, name="home"),
	url(r'^pad/(?P<unique_id>\w+)$', views.home2, name="home2"),
	url(r'^save/', views.save, name="save"),

)
