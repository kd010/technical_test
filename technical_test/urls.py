"""technical_test URL Configuration

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
# from django.conf.urls.defaults import *
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from rest_framework import routers

from pets import views as api_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

#API url request
    url(r'^user/', include('pets.urls', namespace='user')),

#main urls 
    url(r'^$', TemplateView.as_view(template_name="pets/login.html")),
    url(r'^signup/$', TemplateView.as_view(template_name="pets/signup.html")),
    # url(r'^login/$', TemplateView.as_view(template_name="pets/login.html")),
    url(r'^dashboard/$', TemplateView.as_view(template_name="pets/dashboard.html")),


    # url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/images/favicon.ico'}),
]


"""
Customized the django admin site header, index_title and site_title changes.
"""
admin.site.site_header = 'Pet portal administration'
admin.site.index_title = 'Pet portal administration'
admin.site.site_title = 'Pet portal admin'