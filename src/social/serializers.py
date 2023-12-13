from rest_framework import serializers
from django.db.models import Sum

from . import models


class SocialTypesSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.SocialTypes
        fields = ['id', 'name', 'attr', 'created_at', 'state']


class SocialSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Social
        fields = ['id', 'link', 'tg_group', 'integration_id', 'organization', 'social_type', 'state']


class SocialPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.SocialPost
        fields = ['id', 'post_date', 'post_id', 'content', 'media_group_id', 'url', 'social_type', 'organization',
                  'state']


class SocialPostStatsSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.SocialPostStats
        fields = ['id', 'views', 'likes', 'comments', 'shares', 'reactions', 'followers', 'social', 'post']
        # depth = 1


class GetSocialPostStatsByDateSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.SocialPostStats
        fields = '__all__'


class GetActiveSocialSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Social
        fields = '__all__'


class GraphSocialPostStatsByDateSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.SocialPost
        fields = '__all__'