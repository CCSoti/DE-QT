from django.conf.urls import patterns, include, url
from django.contrib import admin
from mappingapp import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Working.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^latitude_chart/', views.graph, name='sample_graph'),
    url(r'^coordinates_table/', views.coordinates, name='coordinates_table'),
)
