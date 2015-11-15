from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

from adec.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/docs/', include('django.contrib.admindocs.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),

    url(r'^termsandconditions/$', terms_and_conditions, name='terms_and_conditions'),
    url(r'^how-it-works/$', how_it_works, name='how_it_works'),
    url(r'^$', home, name='home'),
    url(r'^registerprofessional/$', register_professional, name='register_professional'),
    url(r'^thanks/$', thanks, name='thanks'),
    url(r'^registeruser/$', register_user, name='register_user'),
    url(r'^searchresults/$', search_results, name='search_results'),
    url(r'^profile/$', profile, name='profile'),
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.conf.urls.static import static

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
