from rest_framework import viewsets

from .serializers import HorseSerializer
from .models import Horse


class HorseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Horses to be viewed or edited.
    """
    queryset = Horse.objects.all().order_by('-listing_date')
    serializer_class = HorseSerializer
