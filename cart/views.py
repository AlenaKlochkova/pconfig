import rest_framework.permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .cart import Cart


class CartView(APIView):

    permission_classes = [rest_framework.permissions.AllowAny]

    def get(self, request):
        cart = Cart(request)
        response = cart.cart
        return Response(response)







