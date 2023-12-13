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
    date_from = serializers.DateField(read_only=True)
    date_to = serializers.DateField(read_only=True)
    category = serializers.IntegerField(read_only=True)
    region = serializers.IntegerField(read_only=True)
    district = serializers.IntegerField(read_only=True)
    organization = serializers.IntegerField(read_only=True)
    social_type = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.SocialPostStats
        fields = ['date_from', 'date_to', 'category', 'region', 'district', 'organization', 'social_type']


class GetActiveSocialSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Social
        fields = '__all__'


class GraphSocialPostStatsByDateSerializers(serializers.ModelSerializer):
    date_from = serializers.DateField(read_only=True)
    date_to = serializers.DateField(read_only=True)
    category = serializers.IntegerField(read_only=True)
    region = serializers.IntegerField(read_only=True)
    district = serializers.IntegerField(read_only=True)
    organization = serializers.IntegerField(read_only=True)
    social_type = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.SocialPost
        fields = ['date_from', 'date_to', 'category', 'region', 'district', 'organization', 'social_type']

    # def to_representation(self, instance):
    #     response = dict()
    #     date_from = self.context['request'].query_params.get('date_from', None)
    #     date_to = self.context['request'].query_params.get('date_to', None)
    #     print(instance)
    #     post_stats = models.SocialPostStats.objects.filter(post__in=instance)
    #     response[date_from + ' - ' + date_to] = {
    #         'views': post_stats.aggregate(Sum('views'))['views__sum'],
    #         'likes': post_stats.aggregate(Sum('likes'))['likes__sum'],
    #         'shares': post_stats.aggregate(Sum('shares'))['shares__sum'],
    #         'comments': post_stats.aggregate(Sum('comments'))['comments__sum'],
    #         'followers': post_stats.aggregate(Sum('followers'))['followers__sum'],
    #         'reactions': post_stats.aggregate(Sum('reactions'))['reactions__sum'],
    #         'posts': instance.count()
    #     }
    #     return response
