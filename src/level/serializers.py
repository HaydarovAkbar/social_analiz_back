from .models import LevelType, LevelOrganization
from rest_framework import serializers

from organization.models import Organization

class LevelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelType
        fields = "__all__"


class LevelOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelOrganization
        fields = "__all__"


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"

    def to_representation(self, instance):
        response = dict()
        response['id'] = instance.id
        response['organ_name'] = instance.organization.shortname
        return response