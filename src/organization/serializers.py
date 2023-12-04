from . import models
from rest_framework import serializers


class OrganizationSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Organization
        fields = '__all__'