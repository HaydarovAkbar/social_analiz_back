from rest_framework import routers
from django.urls import path, include

from account import views as account_views
from app import views as app_views
from level import views as level_views
from organization import views as organ_views
from social import views as social_views
from utils import views as utils_views

api = routers.DefaultRouter()
# account registeration urls
api.register(r'users', account_views.UserView, basename='users')

# organization registeration urls
api.register(r'organizations', organ_views.OrganizationView, basename='organizations')

# utils registeration urls
api.register(r'state', utils_views.StateView, basename='state')
api.register(r'language', utils_views.LanguageView, basename='language')
api.register(r'category', utils_views.CategoryView, basename='category')
api.register(r'specialization', utils_views.SpecializationView, basename='specialization')
api.register(r'region', utils_views.RegionView, basename='region')
api.register(r'district', utils_views.DistrictView, basename='district')

# social registeration urls
api.register(r'social_types', social_views.SocialTypeView, basename='social_types')
api.register(r'socials', social_views.SocialView, basename='social')
api.register(r'social_post', social_views.SocialPostView, basename='social_post')
api.register(r'social_post_stats', social_views.SocialPostStatsView, basename='social_post_stats')
api.register(r'get_social_post_stats_by_date', social_views.GetSocialPostStatsByDateView,
             basename='get_social_post_stats_by_date')
api.register(r'get_active_social', social_views.GetActiveSocialView, basename='get_active_social')
api.register(r'graph_social_post_stats_by_date', social_views.GraphSocialPostStatsByDateView,
             basename='graph_social_post_stats_by_date')
api.register(r'get_social_count_by_status', social_views.GetSocialConnectCountView,
             basename='get_social_count_by_status')

# level registeration urls
api.register(r'level_type', level_views.LevelTypeViewSet, basename='level_type')
api.register(r'level_average', level_views.LevelOrganizationViewSet, basename='level_average')

urlpatterns = [
    path('', include(api.urls)),
    path('account/login/', account_views.LoginApiView.as_view(), name='login'),
]
  