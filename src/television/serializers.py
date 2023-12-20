from rest_framework import serializers

from .models import FileStatus, TelevisionType, Files


class FileStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileStatus
        fields = '__all__'


class TelevisionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelevisionType
        fields = '__all__'


class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = '__all__'
