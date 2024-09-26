from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.conf import settings
from django.utils.timezone import activate
activate(settings.TIME_ZONE)


# Create your views here.
class PostListView(ListView): #temp_name = post_list.html
    model = Post
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView): #temp_name = post_detail.html, context_object_name = object
    model = Post
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self) -> bool | None: #ensure current user only edits their posts
        post = self.get_object()
        return post.author == self.request.user
    
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('posts')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self) -> bool | None: #ensure current user only edits their posts
        post = self.get_object()
        return post.author == self.request.user
    
class UserPostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post/user_posts.html'
    def get_queryset(self) -> QuerySet[Any]:
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date_posted')

def search_post(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        posts = Post.objects.filter(title__contains = searched) | Post.objects.filter(content__contains = searched).order_by('-date_posted')
        return render(request, 'post/post_search.html', {'searched':searched, 'posts': posts})
    else:
        return render(request, 'post/post_search.html', {})
    