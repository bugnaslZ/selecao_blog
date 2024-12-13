from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category_blog(models.Model):
    title = models.CharField(max_length=250)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Blog(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    image = models.ImageField(upload_to="blog" , default="default.jpg")
    category = models.ManyToManyField(Category_blog)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.user
    
#____________--___________--
