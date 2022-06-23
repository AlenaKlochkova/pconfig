from django.db import models
from django.contrib.auth.models import AbstractUser

#from .catalog_app.models import Processor, Motherboard, Videocard, RAM, Powerunit, Cooler, Case, HDD


class CustomUser(AbstractUser):

    pass

    def __str__(self):
        return self.username

'''
class Order(models.Model):

    user = models.ForeignKey(UserRegistration)
    processor = models.OneToOneField(Processor)
    motherboard = models.OneToOneField(Motherboard)
    videocard = models.OneToOneField(Videocard)
    ram = models.OneToOneField(RAM)
    powerunit = models.OneToOneField(Powerunit)
    cooler = models.OneToOneField(Cooler)
    case = models.OneToOneField(Case)
    hdd = models.OneToOneField(HDD)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class Sample(Order):

    class Meta:
        verbose_name = 'Шаблон'
        verbose_name_plural = 'Шаблоны'
'''