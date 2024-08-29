from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to='seed_pics', default='default_seed_pic.PNG') #to be specified
    content = models.TextField()
    date_posted = models.DateField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} Post'
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})