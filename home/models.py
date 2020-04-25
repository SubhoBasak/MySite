from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	header = models.CharField(max_length = 100)
	text = models.TextField(blank = True)
	image = models.ImageField(upload_to = 'images/', blank = True)
	date = models.DateField('published date')

class Profile(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	dob = models.DateField('birthday_date', blank = True)
	profile_pic = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics/')
	address = models.TextField(blank = True)
	email = models.EmailField(blank = False)
	about = models.TextField(blank = True)
	theme = models.CharField(blank = False, max_length = 20, default= 'light')

# class Friend(models.Model):
# 	user = models.ForeignKey(User, on_delete = models.CASCADE)
# 	friend = models.ForeignKey(User, on_delete = models.CASCADE)