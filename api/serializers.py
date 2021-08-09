from django.db.models import fields
from rest_framework import serializers
from dashboard import models

class AreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Areas
        fields = "__all__"