from . import models
from rest_framework import serializers


class OrganizationSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Organization
        fields = ['id', 'fullname', 'shortname', 'address', 'inn', 'region', 'district', 'state', 'category',
                  'specialization', 'phone_number','accounter', 'leader']