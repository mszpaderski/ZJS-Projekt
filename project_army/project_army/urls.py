# -*- coding: utf-8 -*-

"""project_army URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf.urls import url
from django.contrib import admin

from django.contrib.auth import views as auth_views

from project_army.views import root_page, signup
from character_sheet.views import characters_list, characters_detail, characters_new, equipment_list, equipment_detail, equipment_new

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', root_page, name='home'),
    url(r'^characters/$', characters_list),
    url(r'^characters/new/$', characters_new),
    url(r'^characters/(?P<id>\d+)/$', characters_detail),
    url(r'^characters/update/$', characters_list),
    url(r'^characters/delete/$', characters_list),
    url(r'^equipment/$', equipment_list),
    url(r'^equipment/new/$', equipment_new),
    url(r'^equipment/(?P<id>\d+)/$', equipment_detail),
    url(r'^equipment/update/$', characters_list),
    url(r'^equipment/delete/$', characters_list),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', signup, name='signup'),
]
