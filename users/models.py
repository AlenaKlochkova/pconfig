from django.db import models
from django.contrib.auth.models import AbstractUser

from catalog_app.models import Processor, Motherboard, Case, Cooler, Videocard, HDD, RAM, Powerunit


class CustomUser(AbstractUser):

    pass

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        return self.username


class Order(models.Model):

    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    processor = models.ForeignKey(to=Processor, on_delete=models.SET_NULL, null=True)
    motherboard = models.ForeignKey(to=Motherboard, on_delete=models.SET_NULL, null=True)
    videocard = models.ForeignKey(to=Videocard, on_delete=models.SET_NULL, null=True)
    ram = models.ForeignKey(to=RAM, on_delete=models.SET_NULL, null=True)
    powerunit = models.ForeignKey(to=Powerunit, on_delete=models.SET_NULL, null=True)
    cooler = models.ForeignKey(to=Cooler, on_delete=models.SET_NULL, null=True)
    case = models.ForeignKey(to=Case, on_delete=models.SET_NULL, null=True)
    hdd = models.ForeignKey(to=HDD, on_delete=models.SET_NULL, null=True)
    total_price = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
