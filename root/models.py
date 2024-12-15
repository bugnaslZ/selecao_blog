from django.db import models

# Create your models here.


class Specials(models.Model):
    services = models.CharField(max_length=120)
   
    
    def __str__(self):
        return self.services

    

class Price(models.Model):
    name = models.CharField(max_length=120)
    service = models.ManyToManyField(Specials)

    def __str__(self):
        return self.name

class Service(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    services = models.ManyToManyField(Specials)
    desc = models.TextField()
   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    catalog_file  = models.TextField()
    ctatlog_doc = models.TextField()
    status = models.BooleanField(default=True)

    
    def __str__(self):
        return self.title
    
    def truncate_char(self):
        return self.content[:10]


class Users(models.Model):
    username = models.CharField(max_length=250)
    pssword = models.CharField(max_length=250)
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)

    
    def __str__(self):
        return self.username




class Ability(models.Model):
    name = models.CharField(max_length=250)

    
    def __str__(self):
        return self.name


class Agent(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='root')
    ability = models.ForeignKey(Ability, on_delete=models.CASCADE)
    x = models.TextField(blank=True, max_length=250)
    instagram = models.TextField(blank=True, max_length=250)
    linkedin = models.TextField(blank=True, max_length=250)
    twitter = models.TextField(blank=True, max_length=250)
    status = models.BooleanField(default=True)

    
  




class About(models.Model):
    title = models.CharField(max_length=250)
    content = models.CharField(max_length=250)
   
    
    def __str__(self):
        return self.title

class Ferquintly(models.Model):
    question = models.TextField()
    answer = models.TextField()

    
    def __str__(self):
        return self.question

class Category_portofilio(models.Model):
    title = models.TextField()

    
    def __str__(self):
        return self.title




class Portfolio(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    name = models.CharField( max_length=250)
    title = models.CharField(max_length=250)
    image = models.ImageField(default='default.jpg', upload_to='root')
    content = models.CharField(max_length=250)
    desc = models.CharField(max_length=250)
   
   
    logo = models.ImageField(default='default.jpg', upload_to='root')
   
    updated_at = models.DateField(auto_now=True)

    
    def __str__(self):
        return self.name


class Stars(models.Model):
    count = models.IntegerField(default=5)


    def __str__(self):
        return str(self.count)




class Tester(models.Model):
    title = models.CharField(max_length=220)
    context = models.CharField(max_length=220)
    logo = models.ImageField(default='default.jpg', upload_to='root')
    domain = models.CharField(max_length=220)
    stars = models.ForeignKey(Stars,on_delete=models.DO_NOTHING)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def count_star(self):
        return range(self.stars.count)



    
class Contactus(models.Model):
   name = models.CharField(max_length=50)
   email = models.EmailField()
   subject = models.CharField(max_length=100)
   message = models.TextField()
   
   
   def __str__(self):
      return self.name

    







