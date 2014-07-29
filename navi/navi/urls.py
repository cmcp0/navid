from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    # url(r'^(\d+)&(\d+)&(\d+)$', 'app.views.get', name='get'),
    # url(r'^buscar/$', 'app.views.buscar', name='buscar'),
    url(r'^nuevo/$', 'app.views.nuevo', name = 'nuevo'),
    url(r'^tipo/(\d+)$', 'app.views.tipo', name='tipo'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
