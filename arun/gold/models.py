from django.db import models

# Create your models here.

# create here feedback table
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    message = models.CharField(max_length=1000)
    mobile = models.IntegerField()
    class Meta:
        db_table = "Contact"

# for product create field here
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50)
    price = models.IntegerField()
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.product_name

#image slider field here
class slider(models.Model):
    image = models.FileField(upload_to='images')

# for cart field here
class cart(models.Model):
    product_name = models.CharField(max_length=50)
    username = models.CharField(max_length=150)
    price = models.FloatField()
    image =models.ImageField(upload_to='images')
    idd = models.IntegerField()
    count =models.IntegerField()
    final_price = models.FloatField()

class user_address(models.Model):
    username=models.CharField(max_length=150)
    email=models.EmailField()
    name=models.CharField(max_length=150)
    address1 = models.TextField()
    mobile=models.IntegerField(default=0)
    city =models.CharField(max_length=150)
    state=models.CharField(max_length=150)
    zip=models.IntegerField()

class comment(models.Model):
    idd=models.IntegerField()
    time = models.DateTimeField(auto_now=True)
    desc =models.TextField(default=0)
    uname=models.CharField(max_length=150)
    """def get_absolute_url(self):
        return "/buy/%i/" %self.idd"""