from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend

from . import models
from .pagination import TenPagination, TwentyPagination
from . import serializers


class StateView(viewsets.ModelViewSet):
    queryset = models.State.objects.all().order_by('id')
    serializer_class = serializers.StateSerializers
    pagination_class = TenPagination
    http_method_names = ['get', ]


class LanguageView(viewsets.ModelViewSet):
    queryset = models.Language.objects.all().order_by('id')
    serializer_class = serializers.LanguageSerializers
    pagination_class = TenPagination
    http_method_names = ['get', ]


class CategoryView(viewsets.ModelViewSet):
    queryset = models.Category.objects.all().order_by('id')
    serializer_class = serializers.CategorySerializers
    pagination_class = TenPagination


class SpecializationView(viewsets.ModelViewSet):
    queryset = models.Specialization.objects.all().order_by('id')
    serializer_class = serializers.SpecializationSerializers
    pagination_class = TenPagination


class RegionView(viewsets.ModelViewSet):
    queryset = models.Region.objects.all().order_by('id')
    serializer_class = serializers.RegionSerializers
    pagination_class = TenPagination


class DistrictView(viewsets.ModelViewSet):
    queryset = models.District.objects.all().order_by('id')
    serializer_class = serializers.DistrictSerializers
    pagination_class = TenPagination
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['region', ]

