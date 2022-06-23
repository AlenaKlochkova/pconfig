from django.conf import settings
from catalog_app.models import Processor, Motherboard, Videocard, RAM, Powerunit, Cooler, Case, HDD


class Cart(object):

    def __init__(self, request,
                 processor=None,
                 motherboard=None,
                 videocard=None,
                 ram=None,
                 powerunit=None,
                 cooler=None,
                 case=None,
                 hdd=None):
        self.processor = processor
        self.motherboard = motherboard
        self.videocard = videocard
        self.ram = ram
        self.powerunit = powerunit
        self.cooler = cooler
        self.case = case
        self.hdd = hdd
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def set_attr_dict(self):
        '''Создает словарь, где соединяет пары таблица каталога - атрибут корзины'''
        model_to_cartattr = {Processor: self.processor,
                             Motherboard: self.motherboard,
                             Videocard: self.videocard,
                             RAM: self.ram,
                             Powerunit: self.powerunit,
                             Cooler: self.cooler,
                             Case: self.case,
                             HDD: self.hdd}
        return model_to_cartattr

    def add_to_cart(self, item):
        '''Устанавливает выбранное значение из таблицы в атрибут корзины'''
        model_to_cartattr = self.set_attr_dict()
        model = item.model
        model_to_cartattr[model] = item
        self.save()

    def save(self):
        self.session.modified = True

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def get_status(self):
        '''Возвращает текущее состояние атрибутов корзины'''
        status = self.set_attr_dict()
        response = {}
        for key, value in status.items():
            response[key.__name__] = value
        return response
