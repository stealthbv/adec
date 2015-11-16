from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from adec.apps.accounts.views import CreateUserView, UserProfileView
from adec.apps.booking.views import ProfessionalList, BusinessList, CreateAppointment, ProfessionalDetail, \
    BusinessDetail
from adec.views import home, terms_and_conditions, how_it_works, thanks, register_user, search_results, profile, \
    edit_profile, login, register_professional

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/docs/', include('django.contrib.admindocs.urls')),

    url(r'^accounts/register/$', CreateUserView.as_view(), name='register_user'),
    url(r'^accounts/profile/$', UserProfileView.as_view(), name='user_profile'),
    url(r'^accounts/', include('django.contrib.auth.urls')),

    url(r'^businesses/$', BusinessList.as_view(), name='business_list'),
    url(r'^businesses/(?P<slug>.+)/$', BusinessDetail.as_view(), name='business_detail'),
    url(r'^professionals/$', register_professional, name='professional_list'),
    url(r'^professionals/(?P<slug>.+)/appointment/$', CreateAppointment.as_view(), name='create_appointment'),
    url(r'^professionals/(?P<slug>.+)/$', ProfessionalDetail.as_view(), name='professional_detail'),

    url(r'^termsandconditions/$', terms_and_conditions, name='terms_and_conditions'),
    url(r'^how-it-works/$', how_it_works, name='how_it_works'),

    url(r'^$', home, name='home'),

    url(r'^thanks/$', thanks, name='thanks'),
    url(r'^registeruser/$', register_user, name='register_user'),
    url(r'^searchresults/$', search_results, name='search_results'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^editprofile/$', edit_profile, name='edit_profile'),
    url(r'^login/$', login, name='login'),
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.conf.urls.static import static

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
