from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/category/', null=True, blank=True)
    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='static/images/', null=True, blank=True)
    video = models.FileField(upload_to='static/videos/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=254)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Bidder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    message = models.TextField()
    bid_amount = models.IntegerField()
    duration = models.CharField(max_length=254)
    status = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user
