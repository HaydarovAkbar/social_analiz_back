from rest_framework import serializers

from . import models


class StateSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.State
        fields = ['id', 'name', 'displayname']


class LanguageSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Language
        fields = ['id', 'code', 'name']


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id', 'shortname', 'fullname', 'ordercode', 'code', 'created_at', 'state']


class SpecializationSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Specialization
        fields = ['id', 'shortname', 'fullname', 'ordercode', 'code', 'created_at', 'state']


class RegionSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Region
        fields = ['id', 'shortname', 'fullname', 'order', 'code', 'created_at', 'state']


class DistrictSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.District
        fields = ['id', 'shortname', 'fullname', 'order', 'code', 'created_at', 'state', 'region']


class InstructionCreateSerializers(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = models.Instruction
        fields = ['file', 'content', 'content_uz', 'content_oz', 'content_ru', 'content_en']


class InstructionSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Instruction
        fields = ['id', 'content']
