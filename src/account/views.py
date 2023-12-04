from rest_framework.response import Response
from . import serializers
from . import models
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework import viewsets
from utils.pagination import TenPagination


class LoginApiView(TokenObtainPairView):
    serializer_class = serializers.LogInSerializer


class UserView(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializers
    pagination_class = TenPagination