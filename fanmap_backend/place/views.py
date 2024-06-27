from django.shortcuts import render
from .models import Place
from .serializers import PlaceSerializer
from rest_framework.viewsets import ModelViewSet

class PlaceViewSet(ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
