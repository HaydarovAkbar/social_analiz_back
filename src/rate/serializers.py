from rest_framework import serializers

from . import models


class RatingCriteriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.RatingCriteria
        fields = '__all__'