from . import models
from rest_framework import serializers
from social.models import Social, SocialTypes


class OrganizationSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Organization
        fields = ['id', 'fullname', 'shortname', 'address', 'inn', 'region', 'district', 'state', 'category',
                  'specialization', 'phone_number', 'accounter', 'leader']


class ListOrganizationSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Organization
        fields = ['id', 'fullname', 'shortname', 'address', 'inn', 'region', 'district', 'state', 'category',
                  'specialization', 'phone_number', 'accounter', 'leader']
        depth = 1

    def to_representation(self, instance):
        data = super(ListOrganizationSerializers, self).to_representation(instance)
        data['region'] = instance.region.shortname
        data['district'] = instance.district.shortname
        data['state'] = instance.state.shortname
        data['category'] = instance.category.shortname
        data['specialization'] = instance.specialization.shortname
        return data


class InactiveSocialOrganizationSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Organization
        fields = '__all__'

    def to_representation(self, instance):
        response = dict()
        response['id'] = instance.id
        response['short_name'] = instance.shortname
        response['full_name'] = instance.fullname
        website = SocialTypes.objects.filter(attr='web').first()
        social = Social.objects.filter(organization=instance, social_type=website).first()
        response['website'] = social.link if social else None
        return response