from django.db import models
from .models import OrderStatus
# Create your models here.
class Order(models.model):
    status=models.Foreignkey(
        OrderStatus,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders"
    )

    def __str__(self):
        return f" Order #{self.id} - {self.status.name if self.status else "No status"


