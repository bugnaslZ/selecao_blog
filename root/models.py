from django.db import models

# Create your models here.


class Specials(models.Model):
    services = models.CharField(max_length=120)
    status = models.BinaryField(default=True)
    

class Price(models.Model):
    name = models.CharField(max_length=120)
    service = models.ManyToManyField(Specials)

class Service(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    services = models.ManyToManyField(Specials)
    desc = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='services' )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    catalog_file  = models.TextField()
    ctatlog_doc = models.TextField()
    status = models.BooleanField(default=True)


class Users(models.Model):
    username = models.CharField(max_length=250)
    pssword = models.CharField(max_length=250)
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)




class Ability(models.Model):
    name = models.CharField(max_length=250)



class Agent(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='agents')
    ability = models.ForeignKey(Ability, on_delete=models.CASCADE)
    instagram = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200)
    status = models.BooleanField(default=False)

class Ferquintly(models.Model):
    question = models.TextField()
    answer = models.TextField()

class Category_portofilio(models.Model):
    title = models.TextField()


class Portfolio(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    name = models.CharField( max_length=250)
    title = models.CharField(max_length=250)
    image = models.ImageField(default='default.jpg', upload_to='portfolios')
    content = models.CharField(max_length=250)
    desc = models.CharField(max_length=250)
    ability = models.ForeignKey(Ability,on_delete=models.CASCADE)
    about_user = models.TextField()
    logo = models.ImageField(default='default.jpg', upload_to='portfolios')
    categoty = models.ManyToManyField(Category_portofilio)
    updated_at = models.DateField(auto_now=True)


class Stars(models.Model):
    count = models.IntegerField(default=5)





class Tester(models.Model):
    title = models.CharField(max_length=250)
    context = models.CharField(max_length=250)
    logo = models.ImageField(default='default.jpg', upload_to='root')
    domain = models.CharField(max_length=250)
    stars = models.ManyToManyField(Stars)
    status = models.BooleanField(default=False)


    


    







