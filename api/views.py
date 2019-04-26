from rest_framework import viewsets
from api.models import HmdaOrwa
from api.serializers import HmdaOrwaSerializer

# Create your views here.

class HmdaOrwaViewSet(viewsets.ModelViewSet):
    queryset = HmdaOrwa.objects.all().order_by('state', 'year', 'index')[:5]
    serializer_class = HmdaOrwaSerializer
