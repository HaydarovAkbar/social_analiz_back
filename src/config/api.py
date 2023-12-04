from rest_framework import routers
from django.urls import path, include

from account import views as account_views
from app import views as app_views
from level import views as level_views
from organization import views as organization_views
from social import views as social_views
from utils import views as utils_views

account_router = routers.DefaultRouter()

account_router.register(r'users/', account_views.UserView, basename='users')

urlpatterns = [
    path('account/', include(account_router.urls)),
    path('account/login/', account_views.LoginApiView.as_view(), name='login'),
]
