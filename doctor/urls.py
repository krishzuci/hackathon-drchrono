from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

import views

urlpatterns = [
    url(r'doctors/',views.post_list, name="post_list"),
]