from django.views.generic.base import View
from django.http import JsonResponse
from .cart import Cart


class CartView(View):

    def get(self, request):

        cart = Cart(request)
        status = cart.get_status()
        return JsonResponse(status)




