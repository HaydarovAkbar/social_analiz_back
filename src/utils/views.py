from rest_framework import viewsets, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
import uuid

from . import models
from .pagination import TenPagination
from . import serializers

from .minio.files import MinioClient


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


class InstructionView(viewsets.ModelViewSet):
    queryset = models.Instruction.objects.all()
    serializer_class = serializers.InstructionSerializers
    pagination_class = TenPagination
    http_method_names = ['get', 'post', 'put', 'delete', ]

    def create(self, request, *args, **kwargs):
        data = request.data
        file = data.get('file')
        minio_client = MinioClient()
        file_id = uuid.uuid4()
        file_extention = file.name.split('.')[-1]
        file_length = file.size
        file_minio = minio_client.add_file(file_id, file, file_extention, file_length)
        if not file_minio:
            return Response({'status': "File qo'shib bo'lmadi"}, status=status.HTTP_400_BAD_REQUEST)
        state = models.State.objects.first()
        file_obj = models.Instruction.objects.create(
            file_name=file.name,
            file_id=file_id,
            file_extension=file_extention,
            content=request.data.get('content', None),
            state=state,
        )
        file_obj.save()
        return Response({'status': 'success'}, status=status.HTTP_201_CREATED)


    # def list(self, request, *args, **kwargs):
    #     insturction = models.Instruction.objects.all()
