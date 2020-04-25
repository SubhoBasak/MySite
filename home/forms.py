from django import forms
from .models import Post, Profile

class NewPost(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['header', 'text', 'image']

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['profile_pic', 'dob', 'email', 'address', 'about', 'theme']
