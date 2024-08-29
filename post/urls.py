from django.contrib import admin
from django.urls import path, include
from post import views as post_views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', post_views.PostListView.as_view(), name='posts'),
    path('posts/<username>/', post_views.UserPostListView.as_view(), name='user_posts'),
    path('<int:pk>/', post_views.PostDetailView.as_view(), name='post_detail'),
    path('new/', post_views.PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/update/', post_views.PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', post_views.PostDeleteView.as_view(), name='post_delete'),
    path('search/', post_views.search_post, name='post_search'),
]
