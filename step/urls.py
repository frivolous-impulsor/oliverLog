from django.urls import path
from .views import StepListView, StepCreateView, StepUpdateView, StepDeleteView

urlpatterns = [
    path('<seed_id>/steps/', StepListView.as_view(), name='step_list'),
    path('<seed_id>/create/', StepCreateView.as_view(), name='step_create'),
    path('<seed_id>/<int:pk>/update/', StepUpdateView.as_view(), name='step_update'),
    path('<seed_id>/<int:pk>/delete/', StepDeleteView.as_view(), name='step_delete'),
]