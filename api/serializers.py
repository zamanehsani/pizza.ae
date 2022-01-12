from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from api import views
from dashboard import models
from django.contrib.auth.models import User

class AreaSerializer(serializers.HyperlinkedModelSerializer):
    # id = serializers.ReadOnlyField()
    class Meta:
        model = models.Areas
        fields = "__all__"

class MenuSerializer(serializers.HyperlinkedModelSerializer):
    # id = serializers.ReadOnlyField()
    class Meta:
        model = models.Menu
        fields = "__all__"

class Menu_categorySerializer(serializers.HyperlinkedModelSerializer):
    # id = serializers.ReadOnlyField()
    class Meta:
        model = models.Menu_category
        fields = "__all__"

class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    # id = serializers.ReadOnlyField()
    class Meta:
        model = models.Order_items
        fields = "__all__"
        depth = 2
class OrderSerializer(serializers.ModelSerializer):
    # id = serializers.ReadOnlyField()
    menu_item_set = OrderItemSerializer(read_only=True,many=True)
    class Meta:
        model = models.Order
        fields = "__all__"
        depth = 1

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    # id = serializers.ReadOnlyField()
    class Meta:
        model = models.Profile
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    # id = serializers.ReadOnlyField()
    class Meta:
        model = User
        fields = ['url','id','username','first_name','last_name','email','date_joined']


class RegisterationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password', 'password2']
        extra_kwargs = { 'password': {'write_only': True} }
    
    def save(self):
        user = User(
            email       = self.validated_data['email'],
            username    = self.validated_data['username'],
        )
            # first_name  = self.validated_data['first_name'],
            # last_name   = self.validated_data['last_name'],
        password    = self.validated_data['password']
        password2   = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Password must match.'})
        
        user.set_password(password)
        user.save()
        return user


# class UserGroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = models.Areas
#         fields = "__all__"

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = models.Customer
        fields = "__all__"
