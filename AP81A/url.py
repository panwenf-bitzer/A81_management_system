#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from django.urls import path
from . import views

urlpatterns=[
path('', views.Dashboard , name='A81A_dashboard'),

]