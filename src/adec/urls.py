from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from adec.views import home, terms_and_conditions, how_it_works

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/docs/', include('django.contrib.admindocs.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),

    url(r'^termsandconditions/$', terms_and_conditions, name='terms_and_conditions'),
    url(r'^how-it-works/$', how_it_works, name='how_it_works'),

    url(r'^$', home, name='home'),
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.conf.urls.static import static

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
