from django.forms.widgets import Select
from django.shortcuts import render
from rest_framework import viewsets, permissions
from dashboard import models
from django.contrib.auth.models import User
from api import serializers
from django.views.decorators.csrf import csrf_exempt, csrf_protect


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
    

class ProfileView(viewsets.ModelViewSet):
    queryset = models.Profile.objects.all()    
    serializer_class = serializers.ProfileSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()    
    serializer_class = serializers.UserSerializer

class CustomerView(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
    