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

urlpatterns = [
    path('', include(api.urls)),
    path('account/login/', account_views.LoginApiView.as_view(), name='login'),
]
