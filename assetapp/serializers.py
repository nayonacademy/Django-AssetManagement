from pyexpat import model

from . models import Asset,Distribution,Member
from rest_framework import serializers

class AssetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'

class DistributionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Distribution
        fields = '__all__'

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'