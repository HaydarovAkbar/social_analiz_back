from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.translation import activate
from rest_framework.permissions import IsAuthenticated

from . import models
from utils.pagination import TenPagination
from utils.filters import OrganizationFilterBackend, OrganizationListFilterBackend
from utils.models import State
from . import serializers


class OrganizationView(viewsets.ModelViewSet):
    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializers
    pagination_class = TenPagination
    filter_backends = [OrganizationFilterBackend, ]
    filterset_fields = ['shortname', 'inn', ]

    # permission_classes = [IsAuthenticated, ]

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ListOrganizationSerializers
        return serializers.OrganizationSerializers


class GetOrganizationListView(viewsets.ModelViewSet):
    queryset = models.Organization.objects.all()
    serializer_class = serializers.InactiveSocialOrganizationSerializers
    pagination_class = TenPagination
    filter_backends = [OrganizationListFilterBackend, ]
    filterset_fields = ['region', 'district', 'category']
    permission_classes = [IsAuthenticated, ]

    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return serializers.ListOrganizationSerializers


class OrganizationCountByStatusView(viewsets.ModelViewSet):
    queryset = models.Organization.objects.all()
    serializer_class = serializers.InactiveSocialOrganizationSerializers
    pagination_class = TenPagination
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['region', 'district', 'category']
    # permission_classes = [IsAuthenticated, ]
    http_method_names = ['get', ]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        data = dict()
        data['all'] = queryset.count()
        state = State.objects.first()
        data['active'] = queryset.filter(state=state).count()
        data['inactive'] = queryset.exclude(state=state).count()
        return Response(data, status=status.HTTP_200_OK)