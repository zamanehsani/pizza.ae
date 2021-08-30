from django.db.models import fields
from rest_framework import serializers
from dashboard import models
from django.contrib.auth.models import User

class AreaSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = models.Areas
        fields = "__all__"

class MenuSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = models.Menu
        fields = "__all__"

class Menu_categorySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = models.Menu_category
        fields = "__all__"

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = models.Order
        fields = "__all__"

# class NewOrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Order
#         fields = "__all__"

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = models.Profile
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = User
        fields = "__all__"

# class UserGroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = models.Areas
#         fields = "__all__"

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = models.Customer
        fields = "__all__"
