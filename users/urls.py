""" Define URL Patterns for users"""

from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
	# Login page
	url(r'^login/$', login, {'template_name':'users/login.html'}, name='login'),
	# Log out
	url(r'^logout/$', views.logout_view, name="logout"),
	# Register
	url(r'^register/$', views.register, name="register"),
	# Activate
	url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),

]