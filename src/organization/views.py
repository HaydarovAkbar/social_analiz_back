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
    permission_classes = [IsAuthenticated, ]

    # def list(self, request, *args, **kwargs):
    #     user = request.user
    #     user_lang = user.language.code
    #     print(user_lang)
    #     activate(user_lang)
    #     return super(OrganizationView, self).list(request, *args, **kwargs)
