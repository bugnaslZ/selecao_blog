from django.db import models
from root.models import Users , Agent

# Create your models here.

class Category_blog(models.Model):
    title = models.CharField(max_length=220)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class Tags(models.Model):
    title = models.CharField(max_length=220)

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=220)
    usename = models.ForeignKey(Agent,on_delete=models.CASCADE)
    category = models.ManyToManyField(Category_blog)
    image = models.ImageField(upload_to='blog',default='default.jpg')
    content = models.TextField()
    content2= models.TextField()
    content3 = models.TextField()
    name = models.CharField(max_length=220)
    logo = models.ImageField(upload_to='blog',default='default.jpg')
    instagram= models.ForeignKey(Agent,on_delete=models.CASCADE)
    twiter= models.ForeignKey(Agent,on_delete=models.CASCADE)
    facebook= models.ForeignKey(Agent,on_delete=models.CASCADE)
    linkdin= models.ForeignKey(Agent,on_delete=models.CASCADE)
    content_agent = models.TextField()
    tags =models.ManyToManyField(Tags)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


