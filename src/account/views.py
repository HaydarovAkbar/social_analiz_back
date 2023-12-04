from django.shortcuts import render
from rest_framework.response import Response
from . import serializers
from rest_framework_simplejwt.views import TokenObtainPairView
from axes.decorators import axes_dispatch
from django.contrib.auth import authenticate
from rest_framework import status
from .models import User
from organization.models import Organization


# class LoginView(TokenObtainPairView):
#     serializer_class = serializers.LogInSerializer

class LoginView(TokenObtainPairView):
    serializer_class = serializers.LogInSerializer

    @axes_dispatch
    def post(self, request, *args, **kwargs):
        context = {
            'uz_latn': {"error": "Login yoki parol xato!"},
            'uz_cyrl': {"error": "Логин ёки пароль хато!"},
            'ru': {"error": "Ошибка логина или пароля!"},
            'en': {"error": "Access is not available"}
        }
        try:
            username = request.data.get('username', None) or request.query_params.get('username', None)
            password = request.data.get('password', None) or request.query_params.get('password', None)
            user = User.objects.get(username=username, password=password)
            if user:
                user.is_active = True
                user.save()
                refresh = serializers.TokenObtainPairSerializer().get_token(user)
                user_permission, data = [], {}
                for item in user.get_all_permissions():
                    user_permission.append(item[item.index('.') + 1:])
                group_data = []
                for group in user.groups.all():
                    group_data.append(group.name)
                data['refresh'] = str(refresh)
                data['access'] = str(refresh.access_token)
                data['full_name'] = user.full_name
                data['email'] = user.email
                data['pinfl'] = user.pinfl
                data['language'] = user.language.name if user.language else None
                data['language_id'] = user.language.id if user.language else None
                data['organization'] = Organization.objects.get(organization=user.organization),
                data['organization_id'] = user.organization.id if user.organization else None
                data['stateId'] = user.state.id if user.state else None
                data['username'] = user.username
                data['groups'] = group_data
                data['permissions'] = user_permission
                return Response(data=data, status=status.HTTP_200_OK)
            else:
                return Response(context[request.LANGUAGE_CODE], status=status.HTTP_401_UNAUTHORIZED)
        except Exception:
            return Response(context[request.LANGUAGE_CODE], status=status.HTTP_401_UNAUTHORIZED)
