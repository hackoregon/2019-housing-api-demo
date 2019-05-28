from api.models import NcdbSampleChanges, NcdbSampleYearly, FIPSRecords
from rest_framework import serializers

class NcdbSampleYearlySerializer(serializers.ModelSerializer):
    class Meta:
        model = NcdbSampleYearly
        fields = "__all__" # TODO: replace with individual fields

class NcdbSampleChangesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NcdbSampleChanges
        fields = "__all__" # TODO: replace with individual fields

class FIPSRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FIPSRecords
        fields = "__all__" # TODO: replace with individual fields
