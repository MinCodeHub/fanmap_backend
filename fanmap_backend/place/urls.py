from rest_framework.routers import SimpleRouter 
from django.urls import path, include
from .views import PlaceViewSet

place_router = SimpleRouter(trailing_slash=False)
place_router.register('place', PlaceViewSet, basename='place')

urlpatterns = [
    path('', include(place_router.urls)),
]
