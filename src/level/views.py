from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.utils.translation import activate
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import status

from .models import LevelType, LevelOrganization
from .serializers import LevelTypeSerializer, LevelOrganizationSerializer, OrganizationSerializer, \
    LevelOrganizationForDaySerializer, LevelOrganizationForRangeSerializer
from .params import get_level

from utils.pagination import TenPagination
from utils.filters import LevelFilterBackend

from organization.models import Organization


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
    filter_backends = [LevelFilterBackend, ]
    # permission_classes = [IsAuthenticated]
    http_method_names = ['get', ]

    @swagger_auto_schema(manual_parameters=get_level, responses={200: 'OK'},
                         operation_id='Get level filter', operation_description='Get level filter')
    def list(self, request, *args, **kwargs):
        # user_lang = request.Meta.get('HTTP_ACCEPT_LANGUAGE', 'ru')
        user_lang = 'ru'
        page = request.query_params.get('page', 1)
        limit = request.query_params.get('limit', 10)
        activate(user_lang)
        queryset = self.filter_queryset(self.queryset)
        start_page, end_page = (int(page) - 1) * int(limit), int(page) * int(limit)
        organizations = Organization.objects.filter(id__in=queryset.values_list('organization', flat=True))[
                       start_page:end_page]
        cells, middle, middle_count = dict(), dict(), 0
        rows = OrganizationSerializer(organizations, many=True).data
        cells = LevelOrganizationForDaySerializer(organizations, many=True,
                                                  context={'date_from': request.query_params.get('date_from'),
                                                           'date_to': request.query_params.get('date_to')}).data
        middle = LevelOrganizationForRangeSerializer(organizations, many=True,
                                                     context={'date_from': request.query_params.get('date_from'),
                                                              'date_to': request.query_params.get('date_to')}).data

        response = {
            'rows': rows,
            'cells': cells,
            'middle': middle,
            'middle_row': middle_count,
        }
        return Response(response, status=status.HTTP_200_OK)
