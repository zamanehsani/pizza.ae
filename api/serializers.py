from django.db.models import fields
from rest_framework import serializers
from dashboard import models
from django.contrib.auth.models import User

class AreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Areas
        fields = "__all__"

class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Menu
        fields = "__all__"

class Menu_categorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Menu_category
        fields = "__all__"

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Order
        fields = "__all__"


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Profile
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

# class UserGroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = models.Areas
#         fields = "__all__"