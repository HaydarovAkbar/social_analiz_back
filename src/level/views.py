from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import LevelType, LevelOrganization
from .serializers import LevelTypeSerializer, LevelOrganizationSerializer

from utils.pagination import TenPagination


class LevelTypeViewSet(viewsets.ModelViewSet):
    queryset = LevelType.objects.all()
    serializer_class = LevelTypeSerializer
    pagination_class = TenPagination
    # permission_classes = [IsAuthenticated]
    http_method_names = ['get', ]


class LevelOrganizationViewSet(viewsets.ModelViewSet):
    queryset = LevelOrganization.objects.all()
    serializer_class = LevelOrganizationSerializer
    pagination_class = TenPagination
    # permission_classes = [IsAuthenticated]
    http_method_names = ['get', ]

    def get_queryset(self):
        queryset = LevelOrganization.objects.all()
        date_from = self.request.query_params.get('date_from', None)
        date_to = self.request.query_params.get('date_to', None)
        level = self.request.query_params.get('level', None)
        organization = self.request.query_params.get('organization', None)
        if level is not None:
            queryset = queryset.filter(level=level)
        if organization is not None:
            queryset = queryset.filter(organization=organization)
        return queryset
