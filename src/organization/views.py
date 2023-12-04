from django.shortcuts import render
from . import models
from utils.pagination import TenPagination
from . import serializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class OrganizationView(viewsets.ModelViewSet):
    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializers
    pagination_class = TenPagination