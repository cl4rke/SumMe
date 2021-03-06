from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'summe_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'summe_app.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^file', 'summe_app.views.index'),
    url(r'^link', 'summe_app.views.index_3'),
    url(r'^uploadFile', 'summe_app.views.uploadFile'),
    url(r'^upload_file', 'summe_app.views.upload_file'),

)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
