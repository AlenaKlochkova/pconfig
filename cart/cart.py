from django.conf import settings

from users.models import Order


class Cart:

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {
                 'Processor': None,
                 'Motherboard': None,
                 'Videocard': None,
                 'RAM': None,
                 'Powerunit': None,
                 'Cooler': None,
                 'Case': None,
                 'HDD': None}
        self.cart = cart

    def add_to_cart(self, item):
        model = item['cat_name']
        self.cart[model] = item['data']
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def remove(self, item):
        model = item['cat_name']
        self.cart[model] = None
        self.save()

    def get_total_price(self):
        total_price = 0
        for value in self.cart.values():
            if value:
                total_price += value[0]['price']
        return total_price

    def create_order(self, request):
        response = {}
        for key, value in self.cart.items():
            if value:
                response[key] = value[0]['id']
            else:
                response[key] = value
        Order.objects.create(
            user=request.user,
            processor=response['Processor'],
            motherboard=response['Motherboard'],
            videocard=response['Videocard'],
            ram=response['RAM'],
            powerunit=response['Powerunit'],
            cooler=response['Cooler'],
            case=response['Case'],
            hdd=response['HDD'],
            total_price=self.get_total_price()
        )
        self.clear()
