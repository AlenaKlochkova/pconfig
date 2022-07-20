from django.db import models


class Component(models.Model):

    model = models.CharField("Модель", max_length=50)
    description = models.CharField("Характеристики", max_length=150)
    price = models.PositiveIntegerField("Цена")
    image = models.ImageField(blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.model


class Processor(Component):

    class Meta:
        verbose_name = 'Процессор'
        verbose_name_plural = 'Процессоры'


class Motherboard(Component):

    class Meta:
        verbose_name = 'Материнская плата'
        verbose_name_plural = 'Материнские платы'


class Videocard(Component):

    class Meta:
        verbose_name = 'Видеокарта'
        verbose_name_plural = 'Видеокарты'


class RAM(Component):

    class Meta:
        verbose_name = 'Оперативная память'


class Powerunit(Component):

    class Meta:
        verbose_name = 'Блок питания'
        verbose_name_plural = 'Блоки питания'


class Cooler(Component):

    class Meta:
        verbose_name = 'Кулер'
        verbose_name_plural = 'Кулеры'


class HDD(Component):

    class Meta:
        verbose_name = 'Жесткий диск'
        verbose_name_plural = 'Жесткие диски'


class Case(Component):

    class Meta:
        verbose_name = 'Корпус'
        verbose_name_plural = 'Корпуса'
