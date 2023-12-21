from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from . import models
from .pagination import TenPagination
from . import serializers


class StateView(viewsets.ModelViewSet):
    queryset = models.State.objects.all()
    serializer_class = serializers.StateSerializers
    pagination_class = TenPagination
    http_method_names = ['get', ]


class LanguageView(viewsets.ModelViewSet):
    queryset = models.Language.objects.all()
    serializer_class = serializers.LanguageSerializers
    pagination_class = TenPagination
    http_method_names = ['get', ]


class CategoryView(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializers
    pagination_class = TenPagination


class SpecializationView(viewsets.ModelViewSet):
    queryset = models.Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializers
    pagination_class = TenPagination


class RegionView(viewsets.ModelViewSet):
    queryset = models.Region.objects.all()
    serializer_class = serializers.RegionSerializers
    pagination_class = TenPagination


class DistrictView(viewsets.ModelViewSet):
    queryset = models.District.objects.all()
    serializer_class = serializers.DistrictSerializers
    pagination_class = TenPagination
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['region', ]

