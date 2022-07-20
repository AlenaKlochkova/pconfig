import rest_framework.permissions
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response

from .cart import Cart


class CartView(APIView):

    permission_classes = [rest_framework.permissions.AllowAny]

    def get(self, request):
        cart = Cart(request)
        if request.cat_name:
            cat_name = request.cat_name
            cart_data = cart.cart[cat_name]
        else:
            cart_data = cart.cart
        response = {'cart': cart_data, 'total_price': cart.get_total_price()}
        return Response(response)

    def delete(self, request):
        cart = Cart(request)
        cart.clear()
        return redirect('home')

    def patch(self, request):
        cart = Cart(request)
        item = request.data
        cart.remove(item)
        return redirect('home')

    def post(self, request):
        permission_classes = [rest_framework.permissions.IsAuthenticated]
        cart = Cart(request)
        cart.create_order(request)
        return redirect('home')

















