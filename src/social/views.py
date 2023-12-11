from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend

from . import models
from utils.pagination import TenPagination, TwentyPagination
from . import serializers


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
