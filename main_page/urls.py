"""Defines URL patterns for main page."""

from django.conf.urls import url

from . import views

urlpatterns = [
	# Home Page
	url(r'^$', views.index, name='index'),
]