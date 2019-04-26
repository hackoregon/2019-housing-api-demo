from api.models import HmdaOrwa
from rest_framework import serializers

class HmdaOrwaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HmdaOrwa
        fields = "__all__"
