from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name='login'),
    path('confirm_logout/', views.confirm_logout, name='confirm_logout'),
    path('logout/', views.UserLogout, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('profile_update/', views.profile_update, name='profile_update'),
]