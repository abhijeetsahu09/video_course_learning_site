from django.db import models

# Create your models here.

class Registered_users(models.Model):
    Date_Created = models.DateField(auto_now_add = True)
    Username = models.CharField(max_length = 100)
    Email = models.EmailField(max_length = 500, unique = True)
    DOB = models.DateField(auto_now_add = False)
    Password = models.CharField(max_length = 50)