from django.shortcuts import render
from rest_framework import viewsets, permissions
from dashboard import models
from api import serializers

class AreaView(viewsets.ModelViewSet):
    queryset = models.Areas.objects.all()
    serializer_class = serializers.AreaSerializer
    