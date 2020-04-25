import random
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import generic
from django.contrib.auth import views as auth_views
from .models import Post, Profile
from django.contrib.auth.forms import UserCreationForm
from .forms import NewPost, ProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
	recent_post = Post.objects.order_by('-date')[:10]
	try:
		if request.user.profile_set.get(pk = request.user.id).theme == 'light':
			base_template = 'light_theme.html'
		else:
			base_template = 'dark_theme.html'
	except Profile.DoesNotExist:
		base_template = 'light_theme.html'
	return render(request, 'index.html', {'posts': recent_post, 'base_template': base_template})

class LoginView(auth_views.LoginView):
	template_name = 'login.html'

class LogoutView(auth_views.LogoutView):
	template_name = 'logout.html'

@login_required
def profile(request, user_id):
	try:
		if request.user.profile_set.get(pk = request.user.id).theme == 'light':
			base_template = 'light_theme.html'
		else:
			base_template = 'dark_theme.html'
	except Profile.DoesNotExist:
		base_template = 'light_theme.html'

	if request.user.id == user_id:
		return render(request, 'profile_form.html', {'form': ProfileForm, 'base_template': base_template})
	else:
		try:
			prof = Profile.objects.get(user__id = user_id)
		except Profile.DoesNotExist:
			raise HttpResponse('No profile found!')
		return render(request, profile, {'data': prof, 'base_template': base_template})

def register(request):
	return render(request, 'register.html', {'form': UserCreationForm})

@login_required
def newpost(request):
	try:
		if request.user.profile_set.get(pk = request.user.id).theme == 'light':
			base_template = 'light_theme.html'
		else:
			base_template = 'dark_theme.html'
	except Profile.DoesNotExist:
		base_template = 'light_theme.html'
	return render(request, 'post_create.html', {'form': NewPost, 'base_template': base_template})

def friends(request):
	pass