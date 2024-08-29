from django.urls import path
from .views import homeView, SeedsListView, SeedDetailView, SeedCreateView, SeedUpdateView,SeedDeleteView, UserPostedSeeds, search_seed

urlpatterns = [
    path('home', homeView, name='home'),
    path('', SeedsListView.as_view(), name='seed_list'),
    path('<int:pk>/', SeedDetailView.as_view(), name='seed_detail'),
    path('create/', SeedCreateView.as_view(), name='seed_create'),
    path('<int:pk>/update/', SeedUpdateView.as_view(), name='seed_update'),
    path('<int:pk>/delete/', SeedDeleteView.as_view(), name='seed_delete'),
    path('<username>/seeds', UserPostedSeeds.as_view(), name='user_seeds'),
    path('search_seed/', search_seed, name='search_seed'),
]