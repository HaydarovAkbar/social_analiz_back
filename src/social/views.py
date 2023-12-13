from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum
from drf_yasg.utils import swagger_auto_schema

from . import models
from . import serializers
from .models import SocialPost, SocialPostStats, Social, SocialTypes
from .params import default_and_date_params, filter_default_params

from organization.models import Organization
from utils.models import State
from utils.pagination import TenPagination, TwentyPagination
from utils.filters import SocialPostFilterByDateBackend, ActiveSocialFilterBackend


class SocialTypeView(viewsets.ModelViewSet):
    queryset = models.SocialTypes.objects.all()
    serializer_class = serializers.SocialTypesSerializers
    pagination_class = TenPagination
    http_method_names = ['get', ]


class SocialView(viewsets.ModelViewSet):
    queryset = models.Social.objects.all()
    serializer_class = serializers.SocialSerializers
    pagination_class = TenPagination
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['organization', ]


class SocialPostView(viewsets.ModelViewSet):
    queryset = models.SocialPost.objects.all()
    serializer_class = serializers.SocialPostSerializers
    pagination_class = TenPagination
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['social_type', 'post_date']


class SocialPostStatsView(viewsets.ModelViewSet):
    queryset = models.SocialPostStats.objects.all()
    serializer_class = serializers.SocialPostStatsSerializers
    pagination_class = TenPagination
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['social', ]


class GetSocialPostStatsByDateView(viewsets.ModelViewSet):
    queryset = SocialPost.objects.all().order_by('id')
    serializer_class = serializers.GetSocialPostStatsByDateSerializers
    filter_backends = [SocialPostFilterByDateBackend, ]
    http_method_names = ['get', ]

    @swagger_auto_schema(manual_parameters=default_and_date_params, responses={200: 'OK'})
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        response = dict()
        response['posts'] = queryset.count()
        get_post_stats = SocialPostStats.objects.filter(post__in=queryset)
        response['views'] = get_post_stats.aggregate(Sum('views'))['views__sum']
        response['likes'] = get_post_stats.aggregate(Sum('likes'))['likes__sum']
        response['shares'] = get_post_stats.aggregate(Sum('shares'))['shares__sum']
        response['comments'] = get_post_stats.aggregate(Sum('comments'))['comments__sum']
        response['followers'] = get_post_stats.aggregate(Sum('followers'))['followers__sum']
        response['reactions'] = get_post_stats.aggregate(Sum('reactions'))['reactions__sum']
        return Response(response, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class GetActiveSocialView(viewsets.ModelViewSet):
    queryset = Social.objects.all().order_by('id')
    serializer_class = serializers.GetActiveSocialSerializers
    filter_backends = [ActiveSocialFilterBackend, ]
    http_method_names = ['get', ]

    @swagger_auto_schema(manual_parameters=filter_default_params, responses={200: 'OK'})
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        response = dict()
        social_types_count = SocialTypes.objects.filter(state=State.objects.first()).count()
        organization_count = self.filter_queryset(Organization.objects.filter(state=State.objects.first()).count())
        social_count = organization_count * social_types_count
        active_socials = queryset.count()
        socials = dict()
        for social_type in SocialTypes.objects.filter(state=State.objects.first()):
            social = queryset.filter(social_type=social_type)
            socials[social_type.attr] = {'status': social.count() > 0,
                                         'url': social.first().link if social.count() == 1 else None}
        response['socials'] = socials
        response['statistics'] = {
            'active_socials': active_socials,
            'inactive_socials': social_count - active_socials,
        }
        return Response(response, status=status.HTTP_200_OK)
