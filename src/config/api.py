from rest_framework import routers
from django.urls import path, include

from account import views as account_views
from app import views as app_views
from level import views as level_views
from organization import views as organ_views
from social import views as social_views
from utils import views as utils_views
from television import views as tv_views

api = routers.DefaultRouter()

# account registeration urls
api.register(r'users', account_views.UserView, basename='users')

# organization registeration urls
api.register(r'organizations', organ_views.OrganizationView, basename='organizations')
api.register(r'organization_list', organ_views.GetOrganizationListView, basename='organization_list')
api.register(r'org_count_by_status', organ_views.OrganizationCountByStatusView,
                basename='org_count_by_status')

# utils registeration urls
api.register(r'state', utils_views.StateView, basename='state')
api.register(r'language', utils_views.LanguageView, basename='language')
api.register(r'category', utils_views.CategoryView, basename='category')
api.register(r'specialization', utils_views.SpecializationView, basename='specialization')
api.register(r'region', utils_views.RegionView, basename='region')
api.register(r'district', utils_views.DistrictView, basename='district')
api.register(r'instruction', utils_views.InstructionView, basename='instruction')

# social registeration urls
api.register(r'social_types', social_views.SocialTypeView, basename='social_types')
api.register(r'socials', social_views.SocialView, basename='social')
api.register(r'social_post', social_views.SocialPostView, basename='social_post')
api.register(r'social_post_stats', social_views.SocialPostStatsView, basename='social_post_stats')
api.register(r'get_social_post_stats_by_date', social_views.GetSocialPostStatsByDateView,
             basename='get_social_post_stats_by_date')
api.register(r'get_active_social', social_views.GetActiveSocialView, basename='get_active_social')  # satsial_network
api.register(r'graph_social_post_stats_by_date', social_views.GraphSocialPostStatsByDateView,
             basename='graph_social_post_stats_by_date')  # for stats
api.register(r'get_social_count_by_status', social_views.GetSocialConnectCountView,
             basename='get_social_count_by_status')
api.register(r'get_social_post_by_date', social_views.GetSocialPostByDateViewSet, basename='get_social_post_by_date')
api.register(r'get_top10_organ', social_views.GetTop10OrganizationView,
             basename='get_top10_organ')
api.register(r'get_top10_post', social_views.GetTop10PostView, basename='get_top10_post')
api.register(r'get_connect_by_organization', social_views.SocialConnectionByOrganizationView,
             basename='get_connect_by_organization')

# level registeration urls
api.register(r'level_type', level_views.LevelTypeViewSet, basename='level_type')
api.register(r'level_average', level_views.LevelOrganizationViewSet, basename='level_average')

# television registeration urls
api.register(r'tv_status', tv_views.FileStatusViewSet, basename='tv_status')
api.register(r'tv_type', tv_views.TelevisionTypeViewSet, basename='tv_type')
api.register(r'tv_file', tv_views.FilesViewSet, basename='tv_file')
api.register(r'input_file', tv_views.InputFileViewSet, basename='input_file')

urlpatterns = [
    path('', include(api.urls)),
    path('account/login/', account_views.LoginApiView.as_view(), name='login'),
]
