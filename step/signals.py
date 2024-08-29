from django.db.models.signals import post_save
from seed.models import Seed
from django.dispatch import receiver
from .models import Step

@receiver(post_save, sender=Seed)
def create_initial_step(sender, instance, created, **kwargs):
    if created:
        Step.objects.create(seed = instance, title = 'title', content='content')