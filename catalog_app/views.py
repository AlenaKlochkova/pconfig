from rest_framework import generics

from .models import *
from .serializers import ComponentSerializer


class ProcessorView(generics.ListAPIView):
    queryset = Processor.objects.all()
    serializer_class = ComponentSerializer


class MotherboardView(generics.ListAPIView):
    queryset = Motherboard.objects.all()
    serializer_class = ComponentSerializer


class VideocardView(generics.ListAPIView):
    queryset = Videocard.objects.all()
    serializer_class = ComponentSerializer


class RAMView(generics.ListAPIView):
    queryset = RAM.objects.all()
    serializer_class = ComponentSerializer


class PowerunitView(generics.ListAPIView):
    queryset = Powerunit.objects.all()
    serializer_class = ComponentSerializer


class CoolerView(generics.ListAPIView):
    queryset = Cooler.objects.all()
    serializer_class = ComponentSerializer


class CaseView(generics.ListAPIView):
    queryset = Case.objects.all()
    serializer_class = ComponentSerializer


class HDDView(generics.ListAPIView):
    queryset = HDD.objects.all()
    serializer_class = ComponentSerializer






