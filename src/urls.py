"""eventbookmvp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'src.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home$', 'src.views.home', name='home'),
    url(r'^registerprofessional$', 'src.views.register_professional', name='register_professional'),
    url(r'^registeruser$', 'src.views.register_user', name='register_user'),
    url(r'^termsandconditions$', 'src.views.terms_and_conditions', name='terms_and_conditions'),
    url(r'^howitworks$', 'src.views.how_it_works', name='how_it_works'),
]
