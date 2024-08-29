from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Seed
from django.urls import reverse_lazy
from users.models import User
from post.models import Post

# Create your views here.
def homeView(request):
    seed_num = Seed.objects.count()
    user_num = User.objects.count()
    post_num = Post.objects.count()
    return render(request, "seed/home.html", {"seed_num": seed_num, "user_num": user_num, "post_num": post_num})

class SeedsListView(ListView):
    model = Seed
    context_object_name = 'seeds'
    template_name = 'seed_list.html'

class SeedDetailView(DetailView):
    model = Seed
    context_object_name = 'seed'

class SeedCreateView(LoginRequiredMixin, CreateView):
    model = Seed
    fields = ['seedName', 'content', 'seedImg', 'obtainTime', 'plantImg', 'growthRate', 'edibleFruit']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class SeedUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Seed
    fields = ['seedName', 'content', 'seedImg', 'obtainTime', 'plantImg', 'growthRate', 'edibleFruit']
    def test_func(self) -> bool | None: #ensure current user only edits their posts
        post = self.get_object()
        return post.author == self.request.user

class SeedDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Seed
    success_url = reverse_lazy('seed_list')
    def test_func(self) -> bool | None: #ensure current user only edits their posts
        post = self.get_object()
        return post.author == self.request.user
    
class UserPostedSeeds(ListView):
    model = Seed
    context_object_name = 'seeds'
    template_name = 'seed/user_seeds.html'
    def get_queryset(self) -> QuerySet[Any]:
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Seed.objects.filter(author = user).order_by('-date_posted')
    
def search_seed(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        seeds = Seed.objects.filter(content__contains = searched) | Seed.objects.filter(seedName__contains = searched) | Seed.objects.filter(obtainTime__contains = searched)
        return render(request, 'seed/search_seed.html', {'searched': searched, 'seeds': seeds})
    else:
        return render(request, 'seed/search_seed.html', {})