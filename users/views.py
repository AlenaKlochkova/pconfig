from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import redirect
from rest_framework import generics, status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import CustomUser
from .serializers import UserSerializer
#from pconfig.cart.cart import Cart


@receiver(post_save, sender=CustomUser)
def init_new_user(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)


class UserViewSet(viewsets.ModelViewSet):
    model = CustomUser
    serializer_class = UserSerializer

    def retrieve(self, request, pk=None):
        if pk == 'me':
            return Response(UserSerializer(request.user).data)
        return super(UserViewSet, self).retrieve(request, pk)


#class OrderView(View):

    #@login_required
    #def make_order(self, request):
        #...
