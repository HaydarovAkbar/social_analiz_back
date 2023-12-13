from .models import LevelType, LevelOrganization
from rest_framework import serializers


class LevelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelType
        fields = "__all__"


class LevelOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelOrganization
        fields = "__all__"
