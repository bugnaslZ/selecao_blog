from django.db import models
from root.models import Users , Agent

# Create your models here.

class category_blog(models.Model):
    title = models.CharField(max_length=220)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class Tags(models.Model):
    title = models.CharField(max_length=220)

    def __str__(self):
        return self.title

class Blog(models.Model):
    agent = models.ForeignKey(Agent,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="blog" , default="default.jpg")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.user
    

class Detail_blog(models.Model):
    title = models.CharField(max_length=220)
    image = models.ImageField(default='default.jpg')
    image2 = models.ImageField(default='default.jpg')
    
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    content2 = models.TextField()
    content3 = models.TextField()
    name = models.CharField(max_length=200)
    name2 = models.CharField(max_length=200)
    logo =models.ImageField(default='default.jpg')
    instagram = models.CharField(max_length=220)
    linkdin = models.CharField(max_length=220)
    twiter = models.CharField(max_length=220)
    facebook = models.CharField(max_length=220)
    content_agent = models.TextField()
    categories = models.ManyToManyField(category_blog)
    tags = models.ManyToManyField(Tags)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
