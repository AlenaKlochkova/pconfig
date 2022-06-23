from django.shortcuts import redirect, render
from django.views.generic.base import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .forms import UserRegistration
from .models import CustomUser
#from pconfig.cart.cart import Cart


class RegistrationView(View):

    def get(self, request):
        response = {}
        fields = UserRegistration.Meta.fields
        for el in fields:
            response[el] = None
        return JsonResponse(response)

    def post(self, request):
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            ...


#class OrderView(View):

    #@login_required
    #def make_order(self, request):
        #...
