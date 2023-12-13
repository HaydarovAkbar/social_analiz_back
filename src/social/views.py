from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework import generics

from . import models
from utils.pagination import TenPagination, TwentyPagination
from . import serializers
from utils.filters import SocialPostFilterByDateBackend
from .models import SocialPost, SocialPostStats


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


class GetSocialPostStatsByDate(viewsets.ModelViewSet):
    queryset = SocialPost.objects.all().order_by('id')
    serializer_class = serializers.GetSocialPostStatsByDateSerializers
    filter_backends = [SocialPostFilterByDateBackend, DjangoFilterBackend]
    filter_fields = ['date_from', 'date_to', 'category', 'region', 'district', 'organization', 'social_type', ]
    http_method_names = ['get', ]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('date_from', openapi.IN_QUERY, description="Start date", type=openapi.TYPE_STRING),
            openapi.Parameter('date_to', openapi.IN_QUERY, description="End date", type=openapi.TYPE_STRING),
            openapi.Parameter('category', openapi.IN_QUERY, description="Category id", type=openapi.TYPE_INTEGER),
            openapi.Parameter('region', openapi.IN_QUERY, description="Region id", type=openapi.TYPE_INTEGER),
            openapi.Parameter('district', openapi.IN_QUERY, description="District id", type=openapi.TYPE_INTEGER),
            openapi.Parameter('organization', openapi.IN_QUERY, description="Organization id", type=openapi.TYPE_INTEGER),
            openapi.Parameter('social_type', openapi.IN_QUERY, description="Social type id", type=openapi.TYPE_INTEGER),
            # Add other query parameters similarly
        ],
        responses={200: 'OK'}
    )
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        response = dict()
        print(queryset)
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



