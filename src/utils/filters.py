from django_filters.rest_framework import DjangoFilterBackend


class OrganizationFilterBackend(DjangoFilterBackend):
    def filter_queryset(self, request, queryset, view):
        user_lang = request.user.language.code
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

        if date_from:
            queryset = queryset.filter(created_at__gte=date_from)
        if date_to:
            queryset = queryset.filter(created_at__lte=date_to)
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