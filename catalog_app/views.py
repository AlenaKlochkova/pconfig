from django.shortcuts import redirect
from rest_framework.views import APIView
import rest_framework.permissions
from rest_framework.response import Response

from .models import *
from .serializers import ComponentSerializer
from cart.cart import Cart


class ComponentView(APIView):
    def __init__(self):
        self.cat = Component

    permission_classes = [rest_framework.permissions.AllowAny]

    def get(self, request):
        query_set = self.cat.objects.all()
        cat_name = self.cat.__name__
        data = ComponentSerializer(instance=query_set, many=True).data
        response = {'cat_name': cat_name, 'data': data}
        return Response(response)

    def post(self, request):
        item = request.data
        cart = Cart(request)
        cart.add_to_cart(item=item)
        return redirect('home')


class ProcessorView(ComponentView):
    def __init__(self):
        self.cat = Processor


class MotherboardView(ComponentView):
    def __init__(self):
        self.cat = Motherboard


class VideocardView(ComponentView):
    def __init__(self):
        self.cat = Videocard


class RAMView(ComponentView):
    def __init__(self):
        self.cat = RAM


class PowerunitView(ComponentView):
    def __init__(self):
        self.cat = Powerunit


class CoolerView(ComponentView):
    def __init__(self):
        self.cat = Cooler


class CaseView(ComponentView):
    def __init__(self):
        self.cat = Case


class HDDView(ComponentView):
    def __init__(self):
        self.cat = HDD






