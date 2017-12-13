from django.conf.urls import url, include
from rest_framework import routers

from .viewsets import HorseViewSet


router = routers.DefaultRouter()
router.register(r'^', HorseViewSet, base_name='horses')

# Wire up our API using automatic URL routing.
urlpatterns = [
    url(r'^horses', include(router.urls)),
]
