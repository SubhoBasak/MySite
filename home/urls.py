from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
	path('', views.index, name = 'index'),
	path('login/', views.LoginView.as_view(), name = 'login'),
	path('logout/', views.LogoutView.as_view(), name = 'logout'),
	path('register/', views.register, name = 'register'),
	path('profile/<int:user_id>/', views.profile, name = 'profile'),
	path('newpost/', views.newpost, name = 'newpost'),
	path('friends/', views.friends, name = 'friends'),
]