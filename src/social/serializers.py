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


class SocialPostByDateSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.SocialPost
        fields = ['id', 'post_date', 'url', 'organization']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['post_date'] = instance.post_date.strftime('%d.%m.%Y')
        post_stat = models.SocialPostStats.objects.filter(post=instance).last()
        if post_stat:
            response['views'] = post_stat.views
            response['likes'] = post_stat.likes
            response['comments'] = post_stat.comments
            response['shares'] = post_stat.shares
            response['reactions'] = post_stat.reactions
            response['followers'] = post_stat.followers
        else:
            response['views'] = 0
            response['likes'] = 0
            response['comments'] = 0
            response['shares'] = 0
            response['reactions'] = 0
            response['followers'] = 0
        return response


class SocialConnectionSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Social
        fields = ['id', 'social', 'organization', 'state']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['organization_name'] = instance.organization.shortname