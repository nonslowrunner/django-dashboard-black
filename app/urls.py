# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from django.conf.urls import url


urlpatterns = [
    # The home page
    url('^$', views.index, name='home'),
    url('resume', views.index, name='home'),
    url('dash', views.dashboard, name='dash'),
    url('lstm', views.lstm, name='lstm'),
    url('nlp', views.nlp, name='nlp'),
    url('covid19', views.covid19, name='covid19'),



]

