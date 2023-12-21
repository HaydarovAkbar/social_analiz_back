from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
import uuid
from rest_framework.decorators import action

from . import serializers
from . import models
from .params import file_input_params

from utils.pagination import TenPagination, TwentyPagination
from utils.minio import MinioClient
from utils.models import State


class FileStatusViewSet(viewsets.ModelViewSet):
    queryset = models.FileStatus.objects.all()
    serializer_class = serializers.FileStatusSerializer
    # authentication_classes = [IsAuthenticated, ]


class TelevisionTypeViewSet(viewsets.ModelViewSet):
    queryset = models.TelevisionType.objects.all()
    serializer_class = serializers.TelevisionTypeSerializer
    # authentication_classes = [IsAuthenticated, ]


class FilesViewSet(viewsets.ModelViewSet):
    queryset = models.Files.objects.all()
    serializer_class = serializers.FilesSerializer
    # authentication_classes = [IsAuthenticated, ]
    pagination_class = TwentyPagination


class InputFileViewSet(viewsets.ModelViewSet):
    queryset = models.Files.objects.all()
    serializer_class = serializers.InputFileSerializer
    # authentication_classes = [IsAuthenticated, ]
    pagination_class = TwentyPagination

    def create(self, request, *args, **kwargs):
        data = request.data
        file = data.get('file')
        file_status = models.FileStatus.objects.get(attr='created')
        minio_client = MinioClient()
        file_id = uuid.uuid4()
        file_extention = file.name.split('.')[-1]
        file_length = file.size
        file_minio = minio_client.add_file(file_id, file, file_extention, file_length)
        if not file_minio:
            return Response({'status': "File qo'shib bo'lmadi"}, status=status.HTTP_400_BAD_REQUEST)
        state = State.objects.first()
        television_type = models.TelevisionType.objects.get(id=data.get('television_type'))
        file_obj = models.Files.objects.create(
            file_name=file.name,
            file_id=file_id,
            file_extension=file_extention,
            content=request.data.get('content', None),
            state=state,
            organization_id=data.get('organization'),
            post_date=data.get('post_date'),
            television_type=television_type,
            file_status=file_status
        )
        file_obj.save()
        return Response({'status': 'success'}, status=status.HTTP_201_CREATED)
