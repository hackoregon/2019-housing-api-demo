from api.models import NcdbSampleChanges, NcdbSampleYearly, FIPSRecords
from api.serializers import NcdbSampleChangesSerializer, NcdbSampleYearlySerializer, FIPSRecordsSerializer
from django.contrib.postgres.fields import ArrayField
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import list_route
from api.filters import NcdbSampleChangesFilter, NcdbSampleYearlyFilter
from django_filters import rest_framework as filters

class NcdbSampleChangesViewSet(viewsets.ModelViewSet):
    queryset = NcdbSampleChanges.objects.all()
    serializer_class = NcdbSampleChangesSerializer
    filter_class = NcdbSampleChangesFilter
    ordering_fields = '__all__'

class NcdbSampleYearlyViewSet(viewsets.ModelViewSet):
    queryset = NcdbSampleYearly.objects.all()
    serializer_class = NcdbSampleYearlySerializer
    filter_class = NcdbSampleYearlyFilter
    ordering_fields = '__all__'

class FIPSRecordsViewSet(viewsets.ModelViewSet):
    queryset = FIPSRecords.objects.all()
    serializer_class = FIPSRecordsSerializer
    ordering_fields = '__all__'
