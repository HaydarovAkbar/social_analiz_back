"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings
from .api import urlpatterns as api_urls
from django.conf.urls.i18n import i18n_patterns

# bot url
from bot.views import MainView as BotMainView


schema_view = get_schema_view(
    openapi.Info(
        title="Pr Api",
        default_version='v2',
        description="Pr api documentations",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="haydarovakbar640@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    # patterns=[path('api/', include('myapi.urls')), ],
    url=settings.HOST,
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('bot/', BotMainView.as_view()),
]

urlpatterns += i18n_patterns(
    path('api/v1/', include(api_urls)),
)
