from django.core.exceptions import ObjectDoesNotExist
from django.forms.widgets import Select
from django.shortcuts import render
from rest_framework import viewsets, permissions
from dashboard import models
from django.contrib.auth.models import User
from api import serializers
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


class AreaView(viewsets.ModelViewSet):
    queryset = models.Areas.objects.all()
    serializer_class = serializers.AreaSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class MenuView(viewsets.ModelViewSet):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer

class MenuCategoryView(viewsets.ModelViewSet):
    queryset = models.Menu_category.objects.all()
    serializer_class = serializers.Menu_categorySerializer


class OrderView(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()    
    serializer_class = serializers.OrderSerializer

class NewOrderView(viewsets.ModelViewSet):
    queryset = models.Order.objects.filter(status = "ordered")
    serializer_class = serializers.OrderSerializer
    
class OrderItemView(viewsets.ModelViewSet):
    queryset = models.Order_items.objects.all()
    serializer_class = serializers.OrderItemSerializer
    

class ProfileView(viewsets.ModelViewSet):
    queryset = models.Profile.objects.all()    
    serializer_class = serializers.ProfileSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()    
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


# adding a new user
@api_view(['POST',])
def registeration_view(request):
    if request.method=='POST':
        serializer = serializers.RegisterationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Successfully registered a new user.'
            data['email'] = account.email
            data['username'] = account.username
        else:
            data = serializer.errors
        return Response(data)


class CustomerView(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
    