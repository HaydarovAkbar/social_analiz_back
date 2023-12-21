from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
# from django_filters.rest_framework import DjangoFilterBackend
from django.utils.translation import activate
from rest_framework.permissions import IsAuthenticated

from . import models
from utils.pagination import TenPagination
from utils.filters import OrganizationFilterBackend
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
