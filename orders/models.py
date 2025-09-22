from django.db import models
# Create your models here.
class Order(models.model):
   coded=models.CharField(max_lenght=50,unique=True)
   discount=models.DecimalField(max_digits=5,decimal_places=2,help_text="discount percentage")
   created_at=models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return self.code


