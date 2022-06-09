from django.shortcuts import render
from django.views.generic.base import View
from django.http import JsonResponse
from abc import ABC, abstractmethod

from .models import Component, Processor, Motherboard, Videocard, RAM, Powerunit, Cooler, Case, HDD


class ComponentView(View, ABC):

    @abstractmethod
    def __init__(self):
        self.model = Component

    def get(self, request):
        model = self.model
        items = model.objects.all()
        d = {}
        for el in items:
            d[el.pk] = {'model': el.model, 'description': el.description, 'price': el.price}
        response = JsonResponse(d)
        return response


class ProcessorView(ComponentView):

    def __init__(self):
        super().__init__()
        self.model = Processor


class MotherboardView(ComponentView):

    def __init__(self):
        super().__init__()
        self.model = Motherboard


class VideocardView(ComponentView):

    def __init__(self):
        super().__init__()
        self.model = Videocard


class RAMView(ComponentView):

    def __init__(self):
        super().__init__()
        self.model = RAM


class PowerunitView(ComponentView):

    def __init__(self):
        super().__init__()
        self.model = Powerunit


class CoolerView(ComponentView):

    def __init__(self):
        super().__init__()
        self.model = Cooler


class CaseView(ComponentView):

    def __init__(self):
        super().__init__()
        self.model = Case


class HDDView(ComponentView):

    def __init__(self):
        super().__init__()
        self.model = HDD






