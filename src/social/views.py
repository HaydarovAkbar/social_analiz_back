from datetime import datetime, timedelta

from django.utils.translation import activate
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum, Count, Q
from drf_yasg.utils import swagger_auto_schema

from . import models
from . import serializers
from .models import SocialPost, SocialPostStats, Social, SocialTypes
from .params import default_and_date_params, filter_default_params, default_and_sort_params

from organization.models import Organization
from organization.serializers import InactiveSocialOrganizationSerializers
from utils.models import State
from utils.pagination import TenPagination, TwentyPagination
from utils.filters import SocialPostFilterByDateBackend, ActiveSocialFilterBackend


class SocialTypeView(viewsets.ModelViewSet):
    queryset = models.SocialTypes.objects.all()
    serializer_class = serializers.SocialTypesSerializers
    pagination_class = TenPagination
    http_method_names = ['get', ]


class SocialView(viewsets.ModelViewSet):
    queryset = models.Social.objects.all()
    serializer_class = serializers.SocialSerializers
    pagination_class = TenPagination
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['organization', ]


class SocialPostView(viewsets.ModelViewSet):
    queryset = models.SocialPost.objects.all()
    serializer_class = serializers.SocialPostSerializers
    pagination_class = TenPagination
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['social_type', 'post_date']


class SocialPostStatsView(viewsets.ModelViewSet):
    queryset = models.SocialPostStats.objects.all()
    serializer_class = serializers.SocialPostStatsSerializers
    pagination_class = TenPagination
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['social', ]


class GetSocialPostStatsByDateView(viewsets.ModelViewSet):
    queryset = SocialPost.objects.all().order_by('id')
    serializer_class = serializers.GetSocialPostStatsByDateSerializers
    filter_backends = [SocialPostFilterByDateBackend, ]
    http_method_names = ['get', ]

    @swagger_auto_schema(manual_parameters=default_and_date_params, responses={200: 'OK'})
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        response = dict()
        response['posts'] = queryset.count()
        get_post_stats = SocialPostStats.objects.filter(post__in=queryset)
        response['views'] = get_post_stats.aggregate(Sum('views'))['views__sum']
        response['likes'] = get_post_stats.aggregate(Sum('likes'))['likes__sum']
        response['shares'] = get_post_stats.aggregate(Sum('shares'))['shares__sum']
        response['comments'] = get_post_stats.aggregate(Sum('comments'))['comments__sum']
        response['followers'] = get_post_stats.aggregate(Sum('followers'))['followers__sum']
        response['reactions'] = get_post_stats.aggregate(Sum('reactions'))['reactions__sum']
        return Response(response, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class GetActiveSocialView(viewsets.ModelViewSet):
    queryset = Social.objects.all().order_by('id')
    serializer_class = serializers.GetActiveSocialSerializers
    filter_backends = [ActiveSocialFilterBackend, ]
    http_method_names = ['get', ]

    @swagger_auto_schema(manual_parameters=filter_default_params, responses={200: 'OK'})
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        response = dict()
        social_types_count = SocialTypes.objects.filter(state=State.objects.first()).count()
        organization_count = self.filter_queryset(Organization.objects.filter(state=State.objects.first()).count())
        social_count = organization_count * social_types_count
        active_socials = queryset.count()
        socials = dict()
        for social_type in SocialTypes.objects.filter(state=State.objects.first()):
            social_f = queryset.filter(social_type=social_type)
            socials[social_type.attr] = {'status': social_f.count() > 0,
                                         'url': social_f.first().link if social_f.count() == 1 else None}
        response['socials'] = socials
        response['statistics'] = {
            'active_socials': active_socials,
            'inactive_socials': social_count - active_socials,
        }
        return Response(response, status=status.HTTP_200_OK)


class GraphSocialPostStatsByDateView(viewsets.ModelViewSet):
    queryset = SocialPost.objects.all().order_by('id')
    serializer_class = serializers.GraphSocialPostStatsByDateSerializers
    filter_backends = [SocialPostFilterByDateBackend, ]
    http_method_names = ['get', ]

    @swagger_auto_schema(manual_parameters=default_and_date_params, responses={200: 'OK'})
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        date_from = datetime.strptime(request.query_params.get('date_from', None), '%Y-%m-%d')
        date_to = datetime.strptime(request.query_params.get('date_to', None), '%Y-%m-%d')
        response = dict()
        if (date_to - date_from).days < 8:
            for i in range((date_to - date_from).days + 1):
                date = date_from + timedelta(days=i)
                response[date.strftime('%d.%m.%Y')] = {
                    'views': SocialPostStats.objects.filter(post__in=queryset, created_at__date=date).aggregate(
                        Sum('views'))['views__sum'],
                    'likes': SocialPostStats.objects.filter(post__in=queryset, created_at__date=date).aggregate(
                        Sum('likes'))['likes__sum'],
                    'shares': SocialPostStats.objects.filter(post__in=queryset, created_at__date=date).aggregate(
                        Sum('shares'))['shares__sum'],
                    'comments': SocialPostStats.objects.filter(post__in=queryset, created_at__date=date).aggregate(
                        Sum('comments'))['comments__sum'],
                    'followers': SocialPostStats.objects.filter(post__in=queryset, created_at__date=date).aggregate(
                        Sum('followers'))['followers__sum'],
                    'reactions': SocialPostStats.objects.filter(post__in=queryset, created_at__date=date).aggregate(
                        Sum('reactions'))['reactions__sum'],
                    'posts': queryset.filter(created_at__date=date).count()
                }
        elif (date_to - date_from).days < 31:
            # interval 5 days
            interval = 5
            for i in range(0, (date_to - date_from).days + 1, interval):
                date = date_from + timedelta(days=i)
                if (date - date_to).days >= 0:
                    continue
                response[date.strftime('%d.%m.%Y') + ' - ' + (date + timedelta(days=interval - 1)).strftime(
                    '%d.%m.%Y')] = {
                    'views': SocialPostStats.objects.filter(post__in=queryset, created_at__date__range=(
                        date, date + timedelta(days=interval - 1))).aggregate(Sum('views'))['views__sum'],
                    'likes': SocialPostStats.objects.filter(post__in=queryset, created_at__date__range=(
                        date, date + timedelta(days=interval - 1))).aggregate(Sum('likes'))['likes__sum'],
                    'shares': SocialPostStats.objects.filter(post__in=queryset, created_at__date__range=(
                        date, date + timedelta(days=interval - 1))).aggregate(Sum('shares'))['shares__sum'],
                    'comments': SocialPostStats.objects.filter(post__in=queryset, created_at__date__range=(
                        date, date + timedelta(days=interval - 1))).aggregate(Sum('comments'))['comments__sum'],
                    'followers': SocialPostStats.objects.filter(post__in=queryset, created_at__date__range=(
                        date, date + timedelta(days=interval - 1))).aggregate(Sum('followers'))['followers__sum'],
                    'reactions': SocialPostStats.objects.filter(post__in=queryset, created_at__date__range=(
                        date, date + timedelta(days=interval - 1))).aggregate(Sum('reactions'))['reactions__sum'],
                    'posts': queryset.filter(created_at__date__range=(
                        date, date + timedelta(days=interval - 1))).count()
                }
        else:
            # interval 1 month
            interval = 30
            for i in range(0, (date_to - date_from).days + 1, interval):
                date = date_from + timedelta(days=i)
                date_name = date.strftime('%B')
                response[date_name] = {
                    'views': SocialPostStats.objects.filter(post__in=queryset, created_at__date__range=(
                        date, date + timedelta(days=interval - 1))).aggregate(Sum('views'))['views__sum'],
                    'likes': SocialPostStats.objects.filter(post__in=queryset, created_at__date__range=(
                        date, date + timedelta(days=interval - 1))).aggregate(Sum('likes'))['likes__sum'],
                    'shares': SocialPostStats.objects.filter(post__in=queryset, created_at__date__range=(
                        date, date + timedelta(days=interval - 1))).aggregate(Sum('shares'))['shares__sum'],
                    'comments': SocialPostStats.objects.filter(post__in=queryset, created_at__date__range=(
                        date, date + timedelta(days=interval - 1))).aggregate(Sum('comments'))['comments__sum'],
                    'followers': SocialPostStats.objects.filter(post__in=queryset, created_at__date__range=(
                        date, date + timedelta(days=interval - 1))).aggregate(Sum('followers'))['followers__sum'],
                    'reactions': SocialPostStats.objects.filter(post__in=queryset, created_at__date__range=(
                        date, date + timedelta(days=interval - 1))).aggregate(Sum('reactions'))['reactions__sum'],
                    'posts': queryset.filter(created_at__date__range=(
                        date, date + timedelta(days=interval - 1))).count()
                }
        return Response(response, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


# Path: src\social\views.py
class GetSocialConnectCountView(viewsets.ModelViewSet):
    queryset = Social.objects.all().order_by('id')
    serializer_class = serializers.GetActiveSocialSerializers
    filter_backends = [ActiveSocialFilterBackend, ]
    http_method_names = ['get', ]

    @swagger_auto_schema(manual_parameters=filter_default_params, responses={200: 'OK'},
                         operation_id='Get social connect count')
    def list(self, request, *args, **kwargs):
        """Get social connect count"""
        queryset = self.filter_queryset(self.get_queryset())
        response = dict()
        for item in SocialTypes.objects.filter(state=State.objects.first()):
            social_f = queryset.filter(social_type=item)
            social_attr = dict()
            social_count = social_f.filter(state=State.objects.first()).count()
            social_attr['active'] = social_count
            social_attr['inactive'] = Organization.objects.filter(
                state=State.objects.first()).count() - social_count
            response[item.attr] = social_attr
        return Response(response, status=status.HTTP_200_OK)


class GetSocialPostByDateViewSet(viewsets.ModelViewSet):
    queryset = SocialPost.objects.all().order_by('id')
    serializer_class = serializers.SocialPostByDateSerializers
    filter_backends = [SocialPostFilterByDateBackend, ]
    pagination_class = TwentyPagination
    http_method_names = ['get', ]

    @swagger_auto_schema(manual_parameters=default_and_date_params, responses={200: 'OK'},
                         operation_id='Get social post by date')
    def list(self, request, *args, **kwargs):
        """Get social post by date"""
        try:
            lang = request.META.get('HTTP_ACCEPT_LANGUAGE', 'ru')
        except Exception:
            lang = 'ru'
        activate(lang)
        return super().list(request, *args, **kwargs)


class GetTop10OrganizationView(viewsets.ModelViewSet):
    queryset = SocialPost.objects.all().order_by('id')
    serializer_class = serializers.SocialPostByDateSerializers
    filter_backends = [SocialPostFilterByDateBackend, ]
    pagination_class = TwentyPagination
    http_method_names = ['get', ]

    @swagger_auto_schema(manual_parameters=default_and_date_params, responses={200: 'OK'},
                         operation_id='Get Top 10 by filter')
    def list(self, request, *args, **kwargs):
        """Get Top 10 by filter"""
        try:
            lang = request.META.get('HTTP_ACCEPT_LANGUAGE', 'ru')
        except Exception:
            lang = 'ru'
        activate(lang)
        page = int(request.query_params.get('page', 1))
        limit = int(request.query_params.get('limit', 10))
        top_organizations = SocialPost.objects.values('organization__id', 'organization__shortname') \
                                .annotate(total_posts=Count('id')) \
                                .order_by('-total_posts')[page * limit - limit:page * limit]
        return Response(status=status.HTTP_200_OK, data=top_organizations)


class GetTop10PostView(viewsets.ModelViewSet):
    queryset = SocialPost.objects.all().order_by('id')
    serializer_class = serializers.SocialPostByDateSerializers
    filter_backends = [SocialPostFilterByDateBackend, ]
    pagination_class = TwentyPagination
    http_method_names = ['get', ]

    @swagger_auto_schema(manual_parameters=default_and_sort_params, responses={200: 'OK'},
                         operation_id='Get Top 10 by filter')
    def list(self, request, *args, **kwargs):
        """Get Top 10 by filter"""
        try:
            lang = request.META.get('HTTP_ACCEPT_LANGUAGE', 'ru')
        except Exception:
            lang = 'ru'
        activate(lang)
        page = int(request.query_params.get('page', 1))
        limit = int(request.query_params.get('limit', 10))
        ordering = request.query_params.get('ordering', 'views')
        if ordering == 'likes':
            instagram = SocialTypes.objects.get(attr='instagram')
            facebook = SocialTypes.objects.get(attr='facebook')
            top_posts = SocialPost.objects.filter(Q(social_type=instagram) | Q(social_type=facebook)).values('id',
                                                                                                             'post_date',
                                                                                                             'url',
                                                                                                             'organization__shortname') \
                            .annotate(total_likes=Sum('socialpoststats__likes')) \
                            .order_by('-total_likes')[page * limit - limit:page * limit]
        else:
            telegram = SocialTypes.objects.get(attr='telegram')
            youtube = SocialTypes.objects.get(attr='youtube')
            top_posts = SocialPost.objects.filter(Q(social_type=youtube) | Q(social_type=telegram)).values(
                'organization__id',
                'post_date',
                'url',
                'organization__shortname') \
                            .annotate(total_views=Sum('socialpoststats__views')) \
                            .order_by('total_views')[page * limit - limit:page * limit]
        return Response(status=status.HTTP_200_OK, data=top_posts)


class SocialConnectionByOrganizationView(viewsets.ModelViewSet):
    queryset = Social.objects.all()
    serializer_class = serializers.SocialConnectionSerializers
    filter_backends = [ActiveSocialFilterBackend, ]
    http_method_names = ['get', ]

    @swagger_auto_schema(manual_parameters=filter_default_params, responses={200: 'OK'},
                         operation_id='Get social connect by organization')
    def list(self, request, *args, **kwargs):
        """Get social connect by organization"""
        queryset = self.filter_queryset(self.get_queryset())
        try:
            user_lang = request.META.get('HTTP_ACCEPT_LANGUAGE', 'ru')
        except Exception:
            user_lang = 'ru'
        activate(user_lang)
        social_type = request.query_params.get('social_type', None)
        response = dict()
        response['active'] = {
            'count': queryset.filter(state=State.objects.first()).count(),
            'data': serializers.SocialConnectionSerializers(queryset.filter(state=State.objects.first()),
                                                            many=True).data
        }
        inactive_org = Organization.objects.filter(
            Q(social__isnull=True) | ~ Q(social__social_type=models.SocialTypes.objects.get(id=social_type)))
        response['inactive'] = {
            'count': inactive_org.count(),
            'data': InactiveSocialOrganizationSerializers(inactive_org, many=True).data
        }
        return Response(response, status=status.HTTP_200_OK)