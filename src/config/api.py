from rest_framework import routers
from django.urls import path, include

from account import views as account_views
from app import views as app_views
from level import views as level_views
from organization import views as organ_views
from social import views as social_views
from utils import views as utils_views

api = routers.DefaultRouter()
# organ_router = routers.DefaultRouter()

api.register(r'users', account_views.UserView, basename='users')

api.register(r'organizations', organ_views.OrganizationView, basename='organizations')

urlpatterns = [
    path('', include(api.urls)),
    # path('organization/', include(organ_router.urls)),
    path('account/login/', account_views.LoginApiView.as_view(), name='login'),
]
