from rest_framework import serializers

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
        fields = ['id', 'post_date', 'post_id', 'content', 'media_group_id', 'url', 'social', 'organization', 'state']


class SocialPostStatsSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.SocialPostStats
        fields = ['id', 'views', 'likes', 'comments', 'shares', 'reactions', 'followers', 'social']
        depth = 1