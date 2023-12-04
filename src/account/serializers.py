from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class LogInSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        attrs = super().validate(attrs)
        attrs["is_staff"] = self.user.is_staff
        return attrs