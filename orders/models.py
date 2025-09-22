from django.db import models
from .models import OrderStatus
# Create your models here.
class Order(models.model):
   name=models.CharField(max_lenght=50,unique=True)

   def __str__(self):
       return self.name


