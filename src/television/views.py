from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from . import serializers
from . import models

from utils.pagination import TenPagination, TwentyPagination


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
    serializer_class = serializers.FilesSerializer
    # authentication_classes = [IsAuthenticated, ]
    pagination_class = TwentyPagination