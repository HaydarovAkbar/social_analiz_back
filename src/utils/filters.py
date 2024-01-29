from datetime import datetime

from django_filters.rest_framework import DjangoFilterBackend

from utils.models import State


class OrganizationFilterBackend(DjangoFilterBackend):
    def filter_queryset(self, request, queryset, view):
        try:
            user_lang = request.user.language.code
        except Exception:
            user_lang = 'ru'
        shortname = request.query_params.get('shortname', None)
        inn = request.query_params.get('inn', None)
        if shortname:
            if user_lang == 'ru':
                queryset = queryset.filter(shortname_ru__icontains=shortname)
            elif user_lang == 'en':
                queryset = queryset.filter(shortname_en__icontains=shortname)
            elif user_lang == 'uz':
                queryset = queryset.filter(shortname_uz__icontains=shortname)
            else:
                queryset = queryset.filter(shortname_oz__icontains=shortname)
        if inn:
            queryset = queryset.filter(inn__icontains=inn)
        user = request.user
        if user.is_superuser:
            return queryset
        else:
            return queryset.filter(user=user)


class SocialPostFilterByDateBackend(DjangoFilterBackend):
    def filter_queryset(self, request, queryset, view):
        date_from = request.query_params.get('date_from', None)
        date_to = request.query_params.get('date_to', None)
        region = request.query_params.get('region', None)
        district = request.query_params.get('district', None)
        category = request.query_params.get('category', None)
        social_type = request.query_params.get('social_type', None)
        organization = request.query_params.get('organization', None)
        is_connect = request.query_params.get('is_connect', None)

        if date_from and date_to:
            # date_from = datetime.strptime(date_from, '%d.%m.%Y')
            # date_to = datetime.strptime(date_to, '%d.%m.%Y')
            date_from = datetime.strptime(date_from, '%Y-%m-%d')
            date_to = datetime.strptime(date_to, '%Y-%m-%d')
            queryset = queryset.filter(created_at__gte=date_from, created_at__lte=date_to)
        if region and region != 'null':
            queryset = queryset.filter(organization__region=region)
        if district and district != 'null':
            queryset = queryset.filter(organization__district=district)
        if category and category != 'null':
            queryset = queryset.filter(organization__category=category)
        if social_type and social_type != 'null':
            queryset = queryset.filter(social_type=social_type)
        if organization and organization != 'null':
            queryset = queryset.filter(organization=organization)
        if is_connect and is_connect != 'null':
            state = State.objects.first()
            queryset = queryset.filter(state=state)
        return queryset


class ActiveSocialFilterBackend(DjangoFilterBackend):
    def filter_queryset(self, request, queryset, view):
        region = request.query_params.get('region', None)
        district = request.query_params.get('district', None)
        category = request.query_params.get('category', None)
        social_type = request.query_params.get('social_type', None)
        organization = request.query_params.get('organization', None)
        if region:
            queryset = queryset.filter(organization__region=region)
        if district:
            queryset = queryset.filter(organization__district=district)
        if category:
            queryset = queryset.filter(organization__category=category)
        if social_type:
            queryset = queryset.filter(social_type=social_type)
        if organization:
            queryset = queryset.filter(organization=organization)
        return queryset


class LevelFilterBackend(DjangoFilterBackend):
    def filter_queryset(self, request, queryset, view):
        level = request.query_params.get('level', None)
        organization = request.query_params.get('organization', None)
        date_from = request.query_params.get('date_from', None)
        date_to = request.query_params.get('date_to', None)
        region = request.query_params.get('region', None)
        district = request.query_params.get('district', None)
        if level is not None:
            queryset = queryset.filter(level=level)
        if organization is not None:
            queryset = queryset.filter(organization=organization)
        if date_from is not None and date_to is not None:
            date_from = datetime.strptime(date_from, '%d.%m.%Y')
            date_to = datetime.strptime(date_to, '%d.%m.%Y')
            queryset = queryset.filter(created_at__gte=date_from, created_at__lte=date_to)
        if region:
            queryset = queryset.filter(organization__region=region)
        if district:
            queryset = queryset.filter(organization__district=district)
        return queryset
