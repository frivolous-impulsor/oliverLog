from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from PIL import Image
from django_resized import ResizedImageField

# Create your models here.
seasons = [
    ("spring", "spring"),
    ("summer", "summer"),
    ("fall", "fall"),
    ("winter", "winter"),
    ("any season", "any season"),
]

growthRate = [
    ("slow", "slow"),
    ("medium", "medium"),
    ("Fast", "Fast"),
    ("Depends on their mood", "Depends on their mood"),
]

class Seed(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING) #not on_delete
    date_posted = models.DateField(default = timezone.now)
    seedName = models.CharField(max_length=50)
    content = models.TextField()
    seedImg = ResizedImageField(size=[500,300], upload_to='seed_pics', default='default_seed_pic.PNG')
    obtainTime = models.CharField(max_length=20, choices=seasons, default="any season")
    plantImg = ResizedImageField(size=[500,300], upload_to='plant_pics', default='default_plant_pic.PNG')
    growthRate = models.CharField(max_length=30, choices=growthRate, default="Depends on their mood")
    edibleFruit = models.BooleanField(null=False, default = False)

    def __str__(self) -> str:
        return self.seedName
    
    def get_absolute_url(self):
        return reverse("seed_detail", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        super(Seed, self).save(*args, **kwargs)
        simg = Image.open(self.seedImg.path)
        pimg = Image.open(self.plantImg.path)
        if simg.width > 1000 or simg.height > 1000:
            output_size = (1000, 1000)
            simg.thumbnail(output_size)
            simg.save(self.seedImg.path)
        if pimg.width > 1000 or pimg.height > 1000:
            output_size = (1000, 1000)
            pimg.thumbnail(output_size)
            pimg.save(self.plantImg.path)
    
