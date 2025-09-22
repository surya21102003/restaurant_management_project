from django.db import models
class MenuCategory(models.model):
    name=models.CharField(max_length=100,unique=true)

    def __str__(self):
        return self.name
