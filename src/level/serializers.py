from datetime import timedelta, datetime

from django.db.models import Avg

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
        response['organ_name'] = instance.shortname
        return response


class LevelOrganizationForDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"

    def to_representation(self, instance):
        date_from = self.context.get('date_from', None)
        date_to = self.context.get('date_to', None)
        date_from, date_to = datetime.strptime(date_from, '%d.%m.%Y'), datetime.strptime(date_to, '%d.%m.%Y')
        response = dict()
        if (date_to - date_from).days < 8:
            for i in range((date_to - date_from).days + 1):
                day = date_from + timedelta(days=i)
                level_organization = LevelOrganization.objects.filter(organization=instance,
                                                                      created_at__date=day).first()
                if not level_organization:
                    continue
                response[day.strftime('%d.%m.%Y')] = {
                    'level': level_organization.level.name,
                    'type': level_organization.level.rate,
                    'color': level_organization.level.color,
                }
        elif (date_to - date_from).days < 31:
            interval = (date_to - date_from).days // 7
            for i in range(interval + 1):
                date_to = date_from + timedelta(days=i * 7)
                date = date_from + timedelta(days=(i - 1) * 7)
                level_organization_average = LevelOrganization.objects.filter(organization=instance,
                                                                              created_at__date__range=(
                                                                                  date, date_to)).aggregate(
                    Avg('level__rate'))
                if not level_organization_average['level__rate__avg']:
                    new_level = LevelType.objects.filter(rate__gte=0).first()
                    response[date_to.strftime('%d.%m.%Y')] = {
                        'level': new_level.name,
                        'type': new_level.rate,
                        'color': new_level.color,
                    }
                else:
                    level_avarage = level_organization_average['level__rate__avg'] / interval
                    new_level = LevelType.objects.filter(rate__gte=level_avarage).first()
                    response[date_to.strftime('%d.%m.%Y')] = {
                        'level': new_level.name,
                        'type': new_level.rate,
                        'color': new_level.color,
                    }
        else:
            interval = (date_to - date_from).days // 30
            for i in range(interval + 1):
                date_to = date_from + timedelta(days=i * 30)
                level_organization_average = LevelOrganization.objects.filter(organization=instance,
                                                                              created_at__date__range=(
                                                                                  date_from, date_to)).aggregate(
                    Avg('level__rate'))
                if not level_organization_average['level__rate__avg']:
                    new_level = LevelType.objects.filter(rate__gte=0).first()
                    response[date_to.strftime('%d.%m.%Y')] = {
                        'level': new_level.name,
                        'type': new_level.rate,
                        'color': new_level.color,
                    }
                else:
                    level_avarage = level_organization_average['level__rate__avg'] / interval
                    new_level = LevelType.objects.filter(rate__gte=level_avarage).first()
                    response[date_to.strftime('%B')] = {
                        'level': new_level.name,
                        'type': new_level.rate,
                        'color': new_level.color,
                    }
        return {instance.id: response}
