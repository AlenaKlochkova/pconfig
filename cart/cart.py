from django.conf import settings


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
        self.session.modified = True

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

