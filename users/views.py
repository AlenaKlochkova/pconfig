from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import redirect
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .models import CustomUser, Order
from .serializers import UserSerializer, OrderSerializer


@receiver(post_save, sender=CustomUser)
def init_new_user(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)


class UserViewSet(viewsets.ModelViewSet):
    model = CustomUser
    serializer_class = UserSerializer

    def retrieve(self, request, pk=None):
        if pk == 'me':
            if Order.objects.filter(pk='me').exists():
                return Response(OrderSerializer(Order.objects.filter(pk='me')).data)
            else:
                return Response(UserSerializer(request.user).data)
        return super().retrieve(request, pk)
