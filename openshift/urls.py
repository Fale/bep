from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
#    url(r'^$', 'openshift.views.home', name='home'),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^login$', 'django.contrib.auth.views.login'),
    url(r'^logout$', 'canvas.views.logout.user_logout'),
    url(r'^canvas/', include('canvas.urls')),
    url(r'^$', 'canvas.views.canvas.list'),
    url(r'^project/', include('project.urls')),
    url(r'^tenant/', include('tenant.urls')),

)
