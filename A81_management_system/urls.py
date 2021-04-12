"""attandance_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CNC_charts.url')),
    path('AP81A/',include("AP81A.url")),
    path("AP81B/",include("AP81B.url")),
    path("AP81C/",include("AP81C.url")),
    path("AP81D/",include("AP81D.url")),
    path("AP81E/",include("AP81E.url")),
    path("AP81F/",include("AP81F.url")),
]
