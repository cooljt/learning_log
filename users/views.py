# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse 
from django.contrib.auth import logout,login,authenticate
#from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes,force_text
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
# Create your views here.
def logout_view(request):
	"""Log the user out"""
	logout(request)
	return HttpResponseRedirect(reverse('learning_logs:index'))

# def register(request):
# 	"""Register a new user with email notification"""
# 	if request.method != "POST":
# 		# Display blank registration form.
# 		form = SignupForm()
# 	else:
# 		# Process completed form.
# 		form = SignupForm(data=request.POST)
# 		if form.is_valid():
# 			new_user = form.save(commit=False)
# 			new_user.is_active = False
# 			new_user.save()
# 			# Send out email confirmation
# 			current_site = get_current_site(request)
# 			mail_subject = 'Activate your account.'
# 			message = render_to_string('users/acc_active_email.html', {
# 				'user':new_user,
# 				'domain':current_site.domain,
# 				'uid':urlsafe_base64_encode(force_bytes(new_user.pk)),
# 				'token':account_activation_token.make_token(new_user),
# 				})
# 			to_email = form.cleaned_data.get('email')
# 			email = EmailMessage(mail_subject, message, to=[to_email])
# 			email.send()
# 			# Log the user in and the redirect to home page
# 			#authenticated_user = authenticate(username=new_user.username,
# 			#	password=request.POST['password1'])
# 			#login(request, authenticated_user)
# 			return HttpReponse('Please confirm your email address to complete the registration.')
# 			#return HttpResponseRedirect(reverse('learning_logs:index'))

# 	context = {'form':form}
# 	return render(request, 'users/register.html', context)


def register(request):
	"""Register a new user without email notification"""
	if request.method != "POST":
		# Display blank registration form.
		form = SignupForm()
	else:
		# Process completed form.
		form = SignupForm(data=request.POST)
		if form.is_valid():
			new_user.save()
			# Log the user in and the redirect to home page
			authenticated_user = authenticate(username=new_user.username,
				password=request.POST['password1'])
			login(request, authenticated_user)
			return HttpResponseRedirect(reverse('learning_logs:index'))

	context = {'form':form}
	return render(request, 'users/register.html', context)

def activate(request, uidb64, token):
	""" activate account"""
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		login(request, user)
		return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
	else:
		return HttpResponse('Activation link is invalid')